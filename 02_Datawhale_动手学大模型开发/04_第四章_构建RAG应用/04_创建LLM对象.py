import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

# 1. 先加载 .env 里的密钥配置（必须写！）
_ = load_dotenv(find_dotenv())

# 2. 创建 LangChain 兼容的 ChatOpenAI 对象（指向 DeepSeek 地址）
llm = ChatOpenAI(
    model_name="deepseek-v4-pro",                 # 或 "deepseek-chat"
    temperature=0,                                 # 温度系数
    api_key=os.environ.get("DEEPSEEK_API_KEY"),     # 👈 显式传入密钥
    base_url="https://api.deepseek.com"           # 👈 必须指定 DeepSeek 官方地址！
)

# 3. 测试调用（LangChain 推荐使用 .invoke 方法）
response = llm.invoke("请你自我介绍一下自己！")

# 4. 打印回复文本内容
print(response.content)