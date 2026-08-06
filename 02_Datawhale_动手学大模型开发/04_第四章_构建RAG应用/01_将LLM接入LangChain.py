from zhipuai_llm import ZhipuaiLLM
from dotenv import find_dotenv, load_dotenv
import os

# 读取本地/项目的环境变量。
_ = load_dotenv(find_dotenv())

# 获取环境变量 API_KEY
api_key = os.environ["ZHIPUAI_API_KEY"] #填写控制台中获取的 APIKey 信息
zhipuai_model = ZhipuaiLLM(model_name="glm-4-plus", temperature=0.1, api_key=api_key)
print(zhipuai_model.invoke("你好，请你自我介绍一下！"))
