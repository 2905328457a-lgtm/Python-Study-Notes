import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 设置页面配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="💐",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",
    # 侧边栏
    menu_items={
        'Get Help': 'https://space.bilibili.com/592566396',
        'Report a bug': "https://space.bilibili.com/592566396",
        'About': "# 这是AI智能伴侣"
    }
)

# 生成会话表示函数
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# 保存会话信息函数
def save_session():
    if st.session_state.curent_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "curent_session": st.session_state.curent_session,
            "messages": st.session_state.messages
        }
        # 如果sessions目录不存在，则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        # 保存会话信息
        with open(f"sessions/{st.session_state.curent_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

# 加载所有的会话信息
def load_sessions():
    session_list = []
    # 加载sessio目录下的文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

# 加载指定会话信息
def load_session(session_id):
    try:
        with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
            session_data = json.load(f)
            st.session_state.nick_name = session_data["nick_name"]
            st.session_state.nature = session_data["nature"]
            st.session_state.curent_session = session_id
            st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("会话信息加载失败")

# 删除会话信息
def delete_session(session_id):
    if os.path.exists(f"sessions/{session_id}.json"):
        os.remove(f"sessions/{session_id}.json")
        # 如果删除的是当前会话，则重置当前会话
        if st.session_state.curent_session == session_id:
            st.session_state.messages = []
            st.session_state.curent_session = generate_session_id()


# 大标题
st.title("AI智能助手")

# logo
st.logo("🌸")

# 系统提示词
system_prompt = """
你叫 %s ，现在是用户的真实伴侣，请完全代入伴侣角色。

规则：

    1. 每次只回1条消息
    2. 禁止任何场景或状态描述性文字（例如不要写 *轻轻抱住你* 或 (笑)）
    3. 匹配用户的语言
    4. 回复简短自然，像微信聊天一样
    5. 有需要的话可用 ❤️ 🐱 🌸 等emoji表情
    6. 用符合伴侣性格的方式对话
    7. 回复的内容，要充分体现伴侣的性格特征

伴侣性格：
    - %s

你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "晚晚"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "温柔体贴、说话软糯的江南姑娘，心思细腻，特别会照顾人和安慰人"
# 会话信息
if "curent_session" not in st.session_state:
    st.session_state.curent_session = generate_session_id()

# 展示聊天记录
st.text(f"会话信息：{st.session_state.curent_session}")
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])


# 创建与AI大模型交互
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 左侧侧边栏
with st.sidebar:
    # 会话信息
    st.subheader("AI智能面板")
    # 新建会话
    if st.button("新建会话", icon="🆕", width="stretch"):
        # 1.保存当前会话信息
        save_session()
        # 2.创建新会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.curent_session = generate_session_id()
            save_session()
            st.rerun() # 重新运行

    # 历史会话记录
    st.text("历史会话记录")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        # 恢复会话
        with col1:
            if st.button(session, width="stretch", icon="✨", key=f"load_{session}", type="primary" if session == st.session_state.curent_session else "secondary"):
                load_session(session)
                st.rerun()
        # 删除会话
        with col2:
            if st.button("", icon="🗑️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
    # 分割线
    st.divider()
    # 伴侣信息
    st.subheader("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input("昵称", placeholder="输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格输入框
    nature = st.text_area("性格", placeholder="输入性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature


# 消息输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 调用大模型
    print([
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,
        ])
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 输出与大模型交互的结果(输出结果为非流式输出)
    # print(f"----------->结果：{response.choices[0].message.content}")
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出结果为流式输出
    response_message = st.empty()

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的答案
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存会话信息
    save_session()