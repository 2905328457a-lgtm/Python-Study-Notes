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
请判断学生的解决方案是否正确，请通过如下步骤解决这个问题：
步骤：
首先，自己解决问题。
然后将您的解决方案与学生的解决方案进行比较，对比计算得到的总费用与学生计算的总费用是否一致，
并评估学生的解决方案是否正确。
在自己完成问题之前，请勿决定学生的解决方案是否正确。
使用以下格式：
问题：问题文本
学生的解决方案：学生的解决方案文本
实际解决方案和步骤：实际解决方案和步骤文本
学生计算的总费用：学生计算得到的总费用
实际计算的总费用：实际计算出的总费用
学生计算的费用和实际计算的费用是否相同：是或否
学生的解决方案和实际解决方案是否相同：是或否
学生的成绩：正确或不正确
问题：
我正在建造一个太阳能发电站，需要帮助计算财务。
- 土地费用为每平方英尺100美元
- 我可以以每平方英尺250美元的价格购买太阳能电池板
- 我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元;
作为平方英尺数的函数，首年运营的总费用是多少。
学生的解决方案：
设x为发电站的大小，单位为平方英尺。
费用：
1. 土地费用：100x美元
2. 太阳能电池板费用：250x美元
3. 维护费用：100,000+100x=10万美元+10x美元
总费用：100x美元+250x美元+10万美元+100x美元=450x+10万美元
实际解决方案和步骤：
"""

response = get_completion(prompt)
print(response)


