import os
import sys
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

# 使用智谱 Embedding
from zhipuai_embedding import ZhipuAIEmbeddings

# 1. 必须优先读取 .env 密钥
_ = load_dotenv(find_dotenv())


# 定义 get_retriever 函数
def get_retriever():
    embedding = ZhipuAIEmbeddings()
    # 修复相对路径为 ../../（退到根目录找向量库）
    persist_directory = '../../data_base/vector_db/chroma'
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding
    )
    return vectordb.as_retriever(search_kwargs={"k": 3})


# 定义 combine_docs 函数
def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs["context"])


# 定义 get_qa_history_chain 函数
def get_qa_history_chain():
    retriever = get_retriever()

    # 切换为 DeepSeek 大模型配置
    llm = ChatOpenAI(
        model_name="deepseek-v4-pro",
        temperature=0,
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )

    condense_question_system_template = (
        "请根据聊天记录总结用户最近的问题，"
        "如果没有多余的聊天记录则返回用户的问题。"
    )
    condense_question_prompt = ChatPromptTemplate([
        ("system", condense_question_system_template),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ])

    retrieve_docs = RunnableBranch(
        (lambda x: not x.get("chat_history", False), (lambda x: x["input"]) | retriever),
        condense_question_prompt | llm | StrOutputParser() | retriever,
    )

    system_prompt = (
        "你是一个基于私有知识库的智能问答助手。请遵守以下规则回答：\n"
        "1. 如果用户是在日常打招呼（如‘你好’、‘你是谁’、‘你会什么’），请礼貌介绍自己是‘基于南瓜书与Prompt工程的知识库助手’；\n"
        "2. 如果用户提问，请严格基于以下【检索到的上下文】进行回答，不要编造答案；\n"
        "3. 如果【检索到的上下文】中没有相关内容，请回答：‘抱歉，在我的知识库中未找到相关解答。’\n\n"
        "【检索到的上下文】：\n{context}"
    )
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ])

    qa_chain = (
            RunnablePassthrough().assign(context=combine_docs)
            | qa_prompt
            | llm
            | StrOutputParser()
    )

    qa_history_chain = RunnablePassthrough().assign(
        context=retrieve_docs,
    ).assign(answer=qa_chain)

    return qa_history_chain


# 定义 gen_response 函数
def gen_response(chain, input, chat_history):
    response = chain.stream({
        "input": input,
        "chat_history": chat_history
    })
    for res in response:
        if "answer" in res.keys():
            yield res["answer"]


# 定义 main 函数
def main():
    st.markdown('### 🦜🔗 动手学大模型应用开发 - 个人 RAG 知识库')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "qa_history_chain" not in st.session_state:
        st.session_state.qa_history_chain = get_qa_history_chain()

    messages = st.container(height=550)

    for message in st.session_state.messages:
        with messages.chat_message(message[0]):
            st.write(message[1])

    if prompt := st.chat_input("请向知识库提问（如：什么是南瓜书？）"):
        st.session_state.messages.append(("human", prompt))
        with messages.chat_message("human"):
            st.write(prompt)

        answer = gen_response(
            chain=st.session_state.qa_history_chain,
            input=prompt,
            chat_history=st.session_state.messages
        )
        with messages.chat_message("ai"):
            output = st.write_stream(answer)

        st.session_state.messages.append(("ai", output))


# main() 函数调用！！
if __name__ == "__main__":
    main()