import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())

client = OpenAI(
    # This is the default and can be omitted
    # 获取环境变量 OPENAI_API_KEY
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
请生成包括书名、作者和类别的三本虚构的、非真实存在的中文书籍清单，\
并以 JSON 格式提供，其中包含以下键:book_id、title、author、genre。
"""
response = get_completion(prompt)
print(response)
