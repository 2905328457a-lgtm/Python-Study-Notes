import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

# ----------------- 1. 读取环境配置 -----------------
_ = load_dotenv(find_dotenv())

# ----------------- 2. 创建大模型对象（DeepSeek） -----------------
llm = ChatOpenAI(
    model_name="deepseek-v4-pro",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# ----------------- 3. 加载向量数据库与 Embedding -----------------
embedding = ZhipuAIEmbeddings()
persist_directory = '../../data_base/vector_db/chroma'

vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)

# ----------------- 4. 构建检索链 (retrieval_chain) -----------------
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# 定义文档拼接函数：把检索到的 3 段资料用换行符拼成一段大文本
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 组装检索链：检索器 -> 提取并拼接文本
retrieval_chain = retriever | format_docs

# ----------------- 5. 定义 Prompt 模板与终极 RAG 链 -----------------
template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答案。最多使用三句话。尽量使答案简明扼要。请用东北话回答，并在结尾说‘妥了，兄弟！’。
{context}
问题: {input}
"""

prompt = PromptTemplate(template=template)

# LCEL 链式语法合体：并发准备上下文与问题 -> 注入 Prompt -> 提交给大模型 -> 解析为文本
qa_chain = (
    RunnableParallel({"context": retrieval_chain, "input": RunnablePassthrough()})
    | prompt
    | llm
    | StrOutputParser()
)

# ----------------- 6. 终极测试：带有知识库的智能问答！ -----------------
question_1 = "什么是南瓜书？"
question_2 = "Prompt Engineering for Developer是谁写的？"

print("🤖 正在查询问题 1...")
result_1 = qa_chain.invoke(question_1)
print("大模型+知识库回答：")
print(result_1)

print("\n" + "="*50 + "\n")

print("🤖 正在查询问题 2...")
result_2 = qa_chain.invoke(question_2)
print("大模型+知识库回答：")
print(result_2)

print(llm.invoke(question_1).content)
print(llm.invoke(question_2).content)