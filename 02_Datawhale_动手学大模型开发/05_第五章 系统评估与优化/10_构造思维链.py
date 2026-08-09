from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

_ = load_dotenv(find_dotenv())    # read local .env file
zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']
DEEPSEEK_API_KEY = os.environ["DEEPSEEK_API_KEY"]

# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 向量数据库持久化路径
persist_directory = '../../data_base/vector_db/chroma'

# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding
)

# 使用 deepseek-v4-pro 模型
llm = ChatOpenAI(
    model_name="deepseek-v4-pro",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"  # 👈 必须放在 ChatOpenAI 内部！
)

template_v1 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
{context}
问题: {question}
"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template_v1)

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

retrievel_chain = vectordb.as_retriever() | RunnableLambda(combine_docs)

qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    | QA_CHAIN_PROMPT
    | llm
    | StrOutputParser()
)
question = "什么是南瓜书"
result = qa_chain.invoke(question)
print(result)
print("--------------------------")

template_v2 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。你应该使答案尽可能详细具体，但不要偏题。如果答案比较长，请酌情进行分段，以提高答案的阅读体验。
{context}
问题: {question}
有用的回答:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template_v2)
qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    | QA_CHAIN_PROMPT
    | llm
    | StrOutputParser()
)
question = "什么是南瓜书"
result = qa_chain.invoke(question)
print(result)

question = "使用大模型时，构造 Prompt 的原则有哪些"
result = qa_chain.invoke(question)
print(result)
print("---------------------------------------")

template_v3 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。你应该使答案尽可能详细具体，但不要偏题。如果答案比较长，请酌情进行分段，以提高答案的阅读体验。
如果答案有几点，你应该分点标号回答，让答案清晰具体
{context}
问题: {question}
有用的回答:"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context","question"],
                                 template=template_v3)
qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    | QA_CHAIN_PROMPT
    | llm
    | StrOutputParser()
)

question = "我们应该如何去构造一个LLM项目"
result = qa_chain.invoke(question)
print(result)
template_v4 = """
请你依次执行以下步骤：
① 使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答案。
你应该使答案尽可能详细具体，但不要偏题。如果答案比较长，请酌情进行分段，以提高答案的阅读体验。
如果答案有几点，你应该分点标号回答，让答案清晰具体。
上下文：
{context}
问题: 
{question}
有用的回答:
② 基于提供的上下文，反思回答中有没有不正确或不是基于上下文得到的内容，如果有，回答你不知道
确保你执行了每一个步骤，不要跳过任意一个步骤。
"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context","question"],
                                 template=template_v4)
qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    | QA_CHAIN_PROMPT
    | llm
    | StrOutputParser()
)

question = "我们应该如何去构造一个LLM项目"
result = qa_chain.invoke(question)
print(result)
