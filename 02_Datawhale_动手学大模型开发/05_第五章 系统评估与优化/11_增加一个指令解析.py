import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from zhipuai_embedding import ZhipuAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
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
template_v1 = """
请你依次执行以下步骤：
① 使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答案。
你应该使答案尽可能详细具体，但不要偏题。如果答案比较长，请酌情进行分段，以提高答案的阅读体验。
如果答案有几点，你应该分点标号回答，让答案清晰具体。
上下文：
{context}
问题: 
{question}
有用的回答:
② 基于提供的上下文，反思回答中有没有不正确或不是基于上下文得到的内容，如果有，回答你不知道
确保你执行了每一个步骤，不要跳过任意一个步骤。
"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template_v1)

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

retrievel_chain = vectordb.as_retriever() | RunnableLambda(combine_docs)

qa_chain = (
    RunnableParallel(context=retrievel_chain, question=RunnablePassthrough())
    | QA_CHAIN_PROMPT
    | llm
    | StrOutputParser()
)
question = "LLM的分类是什么？给我返回一个 Python List"
result = qa_chain.invoke(question)
print(result)
print("--------------------------------------------")
# 使用第二章讲过的 OpenAI 原生接口
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
def gen_gpt_messages(prompt):
    '''
    构造 GPT 模型请求参数 messages

    请求参数：
        prompt: 对应的用户提示词
    '''
    messages = [{"role": "user", "content": prompt}]
    return messages

def get_completion(prompt, model="deepseek-v4-pro", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=gen_gpt_messages(prompt),
        temperature=temperature,
    )
    if len(response.choices) > 0:
        return response.choices[0].message.content
    return "generate answer error"

prompt_input = '''
请判断以下问题中是否包含对输出的格式要求，并按以下要求输出：
请返回给我一个可解析的Python列表，列表第一个元素是对输出的格式要求，应该是一个指令；第二个元素是去掉格式要求的问题原文
如果没有格式要求，请将第一个元素置为空
需要判断的问题：
{}
不要输出任何其他内容或格式，确保返回结果可解析。
'''
response = get_completion(prompt_input.format(question))
print(response)

prompt_output = '''
请根据回答文本和输出格式要求，按照给定的格式要求对问题做出回答
需要回答的问题：
{}
回答文本：
{}
输出格式要求：
{}
'''
question = 'LLM的分类是什么？给我返回一个 Python List'
# 首先将格式要求与问题拆分
input_lst_s = get_completion(prompt_input.format(question))
# 找到拆分之后列表的起始和结束字符
start_loc = input_lst_s.find('[')
end_loc = input_lst_s.find(']')
rule, new_question = eval(input_lst_s[start_loc:end_loc+1])
# 接着使用拆分后的问题调用检索链
result = qa_chain.invoke(new_question)
result_context = result
# 接着调用输出格式解析
response = get_completion(prompt_output.format(new_question, result_context, rule))
print(response)
