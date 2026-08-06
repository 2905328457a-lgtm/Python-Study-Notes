from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_community.vectorstores import Chroma
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

# ----------------- 1. 读取环境配置 -----------------
_ = load_dotenv(find_dotenv())

# ----------------- 创建大模型对象（DeepSeek） -----------------
llm = ChatOpenAI(
    model_name="deepseek-v4-pro",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# 压缩问题的系统 prompt
condense_question_system_template = (
    "请根据聊天记录完善用户最新的问题，"
    "如果用户最新的问题不需要完善则返回用户的问题。"
    )
# ----------------- 加载向量数据库与 Embedding -----------------
embedding = ZhipuAIEmbeddings()
persist_directory = '../../data_base/vector_db/chroma'

vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)
# ----------------- 构建检索链 (retrieval_chain) -----------------
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# 构造 压缩问题的 prompt template
condense_question_prompt = ChatPromptTemplate([
        ("system", condense_question_system_template),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ])
# 问答链的系统prompt
system_prompt = (
    "你是一个问答任务的助手。 "
    "请使用检索到的上下文片段回答这个问题。 "
    "如果你不知道答案就说不知道。 "
    "请使用简洁的话语回答用户。"
    "\n\n"
    "{context}"
)
# 制定prompt template
qa_prompt = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ]
)
# 构造检索文档的链
# RunnableBranch 会根据条件选择要运行的分支
retrieve_docs = RunnableBranch(
    # 分支 1: 若聊天记录中没有 chat_history 则直接使用用户问题查询向量数据库
    (lambda x: not x.get("chat_history", False), (lambda x: x["input"]) | retriever, ),
    # 分支 2 : 若聊天记录中有 chat_history 则先让 llm 根据聊天记录完善问题再查询向量数据库
    condense_question_prompt | llm | StrOutputParser() | retriever,
)
# 重新定义 combine_docs
def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs["context"]) # 将 docs 改为 docs["context"]
# 定义问答链
qa_chain = (
    RunnablePassthrough.assign(context=combine_docs) # 使用 combine_docs 函数整合 qa_prompt 中的 context
    | qa_prompt # 问答模板
    | llm
    | StrOutputParser() # 规定输出的格式为 str
)
# 定义带有历史记录的问答链
qa_history_chain = RunnablePassthrough.assign(
    context = (lambda x: x) | retrieve_docs # 将查询结果存为 content
    ).assign(answer=qa_chain) # 将最终结果存为 answer
# 不带聊天记录
res1 = qa_history_chain.invoke({
    "input": "西瓜书是什么？",
    "chat_history": []
})
print(res1)
# 带聊天记录
res2= qa_history_chain.invoke({
    "input": "南瓜书跟它有什么关系？",
    "chat_history": [
        ("human", "西瓜书是什么？"),
        ("ai", "西瓜书是指周志华老师的《机器学习》一书，是机器学习领域的经典入门教材之一。"),
    ]
})
print(res2)
