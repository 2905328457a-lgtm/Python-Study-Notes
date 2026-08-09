import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


# 1. 读取环境配置
_ = load_dotenv(find_dotenv())

# 2. 定义 Embeddings 适配器
embedding = ZhipuAIEmbeddings()

# 3. 向量数据库持久化路径
persist_directory = '../../data_base/vector_db/chroma'

# 4. 加载 Chroma 向量数据库
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)
retriever = vectordb.as_retriever()

# 5. 正确初始化 DeepSeek 大模型（将 api_key 和 base_url 放入 ChatOpenAI 参数中）
llm = ChatOpenAI(
    model_name="deepseek-v4-pro",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"  # 👈 必须放在 ChatOpenAI 内部！
)

# 6. 打印检查 LLM 对象
# print(llm)

template_v1 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
{context}
问题: {question}
"""

QA_CHAIN_PROMPT = PromptTemplate(template=template_v1)

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
retrievel_chain = retriever | RunnableLambda(combine_docs)
qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    |{
        "answer": QA_CHAIN_PROMPT | llm | StrOutputParser(),
        "context": lambda x: x["context"]
    }
)
print("问题一：")
question = "南瓜书和西瓜书有什么关系？"
result = qa_chain.invoke(question)
print(result["answer"])

print("问题二：")
question = "应该如何使用南瓜书？"
result = qa_chain.invoke(question)
print(result["answer"])

print("**************************************")

template_v2 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。你应该使答案尽可能详细具体，但不要偏题。如果答案比较长，请酌情进行分段，以提高答案的阅读体验。
{context}
问题: {question}
有用的回答:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template_v2)

qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    | {
        "answer": QA_CHAIN_PROMPT | llm | StrOutputParser(),
        "context": lambda x: x["context"]
    }
)

print("问题一：")
question = "南瓜书和西瓜书有什么关系？"
result = qa_chain.invoke(question)
print(result["answer"])

print("问题二：")
question = "应该如何使用南瓜书？"
result = qa_chain.invoke(question)
print(result["answer"])
