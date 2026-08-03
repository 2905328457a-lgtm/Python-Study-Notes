import os
from openai import OpenAI

# 创建与AI大模型交互
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 交互参数
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名职业规划大师"},
        {"role": "user", "content": "中国未来5年内哪些岗位不会被AI取代"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出与大模型交互的结果
print(response.choices[0].message.content)