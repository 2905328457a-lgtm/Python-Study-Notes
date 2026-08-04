import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# 读取本地/项目的环境变量。
_ = load_dotenv(find_dotenv())

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 导入所需库
# 注意，此处我们假设你已根据上文配置了 OpenAI API Key，如没有将访问失败
completion = client.chat.completions.create(
    # 调用模型：deepseek-v4-pro
    model="deepseek-v4-pro",
    # messages 是对话列表
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! 请用中文向我问好！"}
    ]
)
# 加上这一行，把大模型的文字回答打印到控制台 👇
print(completion.choices[0].message.content)
# 打印完整的原始返回对象 👇
print(completion)
