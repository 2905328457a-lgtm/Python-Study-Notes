import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


# 1. 读取环境配置
_ = load_dotenv(find_dotenv())

# 2. 定义 Embeddings 适配器
embedding = ZhipuAIEmbeddings()

# 3. 向量数据库持久化路径
persist_directory = '../../data_base/vector_db/chroma'

# 4. 加载 Chroma 向量数据库
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)
retriever = vectordb.as_retriever()

# 5. 正确初始化 DeepSeek 大模型（将 api_key 和 base_url 放入 ChatOpenAI 参数中）
llm = ChatOpenAI(
    model_name="deepseek-v4-pro",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"  # 👈 必须放在 ChatOpenAI 内部！
)


def multi_select_score_v1(true_answer : str, generate_answer : str) -> float:
    # true_anser : 正确答案，str 类型，例如 'BCD'
    # generate_answer : 模型生成答案，str 类型
    true_answers = list(true_answer)
    '''为便于计算，我们假设每道题都只有 A B C D 四个选项'''
    # 先找出错误答案集合
    false_answers = [item for item in ['A', 'B', 'C', 'D'] if item not in true_answers]
    # 如果生成答案出现了错误答案
    for one_answer in false_answers:
        if one_answer in generate_answer:
            return 0
    # 再判断是否全选了正确答案
    if_correct = 0
    for one_answer in true_answers:
        if one_answer in generate_answer:
            if_correct += 1
            continue
    if if_correct == 0:
        # 不选
        return 0
    elif if_correct == len(true_answers):
        # 全选
        return 1
    else:
        # 漏选
        return 0.5
answer1 = 'B C'
answer2 = '西瓜书的作者是 A 周志华'
answer3 = '应该选择 B C D'
answer4 = '我不知道'
true_answer = 'BCD'
print("答案一得分：", multi_select_score_v1(true_answer, answer1))
print("答案二得分：", multi_select_score_v1(true_answer, answer2))
print("答案三得分：", multi_select_score_v1(true_answer, answer3))
print("答案四得分：", multi_select_score_v1(true_answer, answer4))
print("--------------------------------------------------------")
def multi_select_score_v2(true_answer : str, generate_answer : str) -> float:
    # true_anser : 正确答案，str 类型，例如 'BCD'
    # generate_answer : 模型生成答案，str 类型
    true_answers = list(true_answer)
    '''为便于计算，我们假设每道题都只有 A B C D 四个选项'''
    # 先找出错误答案集合
    false_answers = [item for item in ['A', 'B', 'C', 'D'] if item not in true_answers]
    # 如果生成答案出现了错误答案
    for one_answer in false_answers:
        if one_answer in generate_answer:
            return -1
    # 再判断是否全选了正确答案
    if_correct = 0
    for one_answer in true_answers:
        if one_answer in generate_answer:
            if_correct += 1
            continue
    if if_correct == 0:
        # 不选
        return 0
    elif if_correct == len(true_answers):
        # 全选
        return 1
    else:
        # 漏选
        return 0.5
answer1 = 'B C'
answer2 = '西瓜书的作者是 A 周志华'
answer3 = '应该选择 B C D'
answer4 = '我不知道'
true_answer = 'BCD'
print("答案一得分：", multi_select_score_v2(true_answer, answer1))
print("答案二得分：", multi_select_score_v2(true_answer, answer2))
print("答案三得分：", multi_select_score_v2(true_answer, answer3))
print("答案四得分：", multi_select_score_v2(true_answer, answer4))
