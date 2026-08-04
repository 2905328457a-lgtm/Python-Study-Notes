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

# 满足条件的输入（text_1 中提供了步骤）
text_1 = f"""
泡一杯茶很容易。首先，需要把水烧开。\
在等待期间，拿一个杯子并把茶包放进去。\
一旦水足够热，就把它倒在茶包上。\
等待一会儿，让茶叶浸泡。几分钟后，取出茶包。\
如果您愿意，可以加一些糖或牛奶调味。\
就这样，您可以享受一杯美味的茶了。
"""
prompt = f"""
您将获得由三个引号括起来的文本。\
如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：
第一步 - ...
第二步 - …
…
第N步 - …
如果文本中不包含一系列的指令，则直接写“未提供步骤”。"
{text_1}
"""
response = get_completion(prompt)
print("Text 1 的总结:")
print(response)

# 不满足条件的输入（text_2 中未提供预期指令）
text_2 = f"""
今天阳光明媚，鸟儿在歌唱。\
这是一个去公园散步的美好日子。\
鲜花盛开，树枝在微风中轻轻摇曳。\
人们外出享受着这美好的天气，有些人在野餐，有些人在玩游戏或者在草地上放松。\
这是一个完美的日子，可以在户外度过并欣赏大自然的美景。
"""
prompt = f"""
您将获得由三个引号括起来的文本。\
如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：
第一步 - ...
第二步 - …
…
第N步 - …
如果文本中不包含一系列的指令，则直接写“未提供步骤”。"
{text_2}
"""
response = get_completion(prompt)
print("Text 2 的总结:")
print(response)
