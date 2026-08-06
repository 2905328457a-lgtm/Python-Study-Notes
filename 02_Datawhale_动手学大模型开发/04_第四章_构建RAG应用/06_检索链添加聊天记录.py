from langchain_core.prompts import ChatPromptTemplate

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
# 无历史记录
messages = qa_prompt.invoke(
    {
        "input": "南瓜书是什么？",
        "chat_history": [],
        "context": ""
    }
)
for message in messages.messages:
    print(message.content)
print("-----------------------------------------------------\n")
# 有历史记录
messages = qa_prompt.invoke(
    {
        "input": "你可以介绍一下他吗？",
        "chat_history": [
            ("human", "西瓜书是什么？"),
            ("ai", "西瓜书是指周志华老师的《机器学习》一书，是机器学习领域的经典入门教材之一。"),
        ],
        "context": ""
    }
)
for message in messages.messages:
    print(message.content)
