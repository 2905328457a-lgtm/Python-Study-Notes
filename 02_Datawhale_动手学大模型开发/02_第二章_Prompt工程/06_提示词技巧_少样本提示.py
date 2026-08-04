import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())

client = OpenAI(
    # This is the default and can be omitted
    # 获取环境变量 DEEPSEEK_API_KEY
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


# 一个封装 DeepSeek 接口的函数，参数为 Prompt，返回对应结果
def get_completion(prompt, model="deepseek-v4-pro"):
    '''
    prompt: 对应的提示词
    model: 调用的模型，默认为 deepseek-v4-pro。
           https://api.deepseek.com
    '''

    messages = [{"role": "user", "content": prompt}]

    # 调用 DeepSeek 的接口
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content

prompt = f"""
你的任务是以一致的风格回答问题（注意：文言文和白话的区别）。
<学生>: 请教我何为耐心。
<圣贤>: 天生我材必有用，千金散尽还复来。
<学生>: 请教我何为坚持。
<圣贤>: 故不积跬步，无以至千里；不积小流，无以成江海。骑骥一跃，不能十步；驽马十驾，功在不舍。
<学生>: 请教我何为孝顺。
"""
response = get_completion(prompt)
print(response)
