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
print(f"向量库中存储的数量：{vectordb._collection.count()}")
question = "什么是prompt engineering?"
retriever = vectordb.as_retriever(search_kwargs={"k": 3})
docs = retriever.invoke(question)
print(f"检索到的内容数：{len(docs)}")
for i, doc in enumerate(docs):
    print(f"检索到的第{i}个内容: \n {doc.page_content}", end="\n-----------------------------------------------------\n")
