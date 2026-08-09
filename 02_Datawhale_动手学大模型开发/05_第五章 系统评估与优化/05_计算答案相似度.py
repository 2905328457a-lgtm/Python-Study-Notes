import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import jieba


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


def bleu_score(true_answer: str, generate_answer: str) -> float:
    # 1. 用 jieba 分词
    true_answers = list(jieba.cut(true_answer))
    generate_answers = list(jieba.cut(generate_answer))

    # 2. 使用 SmoothingFunction 平滑函数（消除 4-gram 匹配为0时的警告）
    smooth_fn = SmoothingFunction().method1

    # 💡 核心修复：true_answers 必须用列表包起来 [true_answers]，并传入平滑函数
    score = sentence_bleu([true_answers], generate_answers, smoothing_function=smooth_fn)
    return score
true_answer = '周志华老师的《机器学习》（西瓜书）是机器学习领域的经典入门教材之一，周老师为了使尽可能多的读者通过西瓜书对机器学习有所了解, 所以在书中对部分公式的推导细节没有详述，但是这对那些想深究公式推导细节的读者来说可能“不太友好”，本书旨在对西瓜书里比较难理解的公式加以解析，以及对部分公式补充具体的推导细节。'

print("答案一：")
answer1 = '周志华老师的《机器学习》（西瓜书）是机器学习领域的经典入门教材之一，周老师为了使尽可能多的读者通过西瓜书对机器学习有所了解, 所以在书中对部分公式的推导细节没有详述，但是这对那些想深究公式推导细节的读者来说可能“不太友好”，本书旨在对西瓜书里比较难理解的公式加以解析，以及对部分公式补充具体的推导细节。'
print(answer1)
score = bleu_score(true_answer, answer1)
print("得分：", score)
print("答案二：")
answer2 = '本南瓜书只能算是我等数学渣渣在自学的时候记下来的笔记，希望能够帮助大家都成为一名合格的“理工科数学基础扎实点的大二下学生”'
print(answer2)
score = bleu_score(true_answer, answer2)
print("得分：", score)
