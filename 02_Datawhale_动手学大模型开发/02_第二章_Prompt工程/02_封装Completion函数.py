import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# 1. 必须先加载 .env 密钥
_ = load_dotenv(find_dotenv())

# 2. 初始化客户端（指向 DeepSeek 官方地址）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# ---------------- 教程中的第一段代码：定义/封装函数 ----------------
def get_completion(prompt, model="deepseek-v4-pro", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    if len(response.choices) > 0:
        return response.choices[0].message.content
    return "generate answer error"


# ---------------- 教程中的第二段代码：调用函数 ----------------
# ⚠️ 注意：在 .py 文件里要加上 print()，控制台才会打出字！
print(get_completion("你好！"))