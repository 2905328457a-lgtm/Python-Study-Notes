import os
from dotenv import load_dotenv, find_dotenv
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_community.vectorstores import Chroma

_ = load_dotenv(find_dotenv())    # read local .env file
zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']

# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 向量数据库持久化路径
persist_directory = '../../data_base/vector_db/chroma'

# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding
)
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

from langchain_core.runnables import RunnableLambda
def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

combiner = RunnableLambda(combine_docs)
retrieval_chain = retriever | combiner

print(retrieval_chain.invoke("南瓜书是什么？"))
