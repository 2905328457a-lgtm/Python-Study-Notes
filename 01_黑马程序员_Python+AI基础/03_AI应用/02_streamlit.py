import streamlit as st

# 设置页面配置项
st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "# 这是streamlit的入门演示"
    }
)

# 大标题
st.title("streamlit入门演示")
st.header("☕ 精品手冲咖啡探索指南")
st.subheader("从豆到杯，感受风味与时间的艺术")
# ----------------- 介绍文案 -----------------
st.write("手冲咖啡（Pour-Over Coffee）不仅是一种饮品制作方式，更是一场关于风味萃取的感官仪式。通过控制水温、研磨度和冲煮节奏，能够最大程度展现咖啡豆原产地独特的果香、花香与酸甜平衡感。")
st.write("豆种选择是决定风味基底的关键。来自埃塞俄比亚耶加雪菲的咖啡豆通常带有迷人的茉莉花香与柑橘酸调；而肯尼亚豆则以明亮的黑加仑风味和浓郁的果酸著称。优质的浅度烘焙能够完美保留这些天然的植物风味。")
st.write("冲煮细节决定成败。推荐使用 90°C - 93°C 的新鲜过滤水，粉水比例保持在 1:15 至 1:16 之间。先进行 30 秒的闷蒸激活咖啡粉风味，再进行分段注水。耐心等待滴滤完成，即可享用一杯香气溢满房间的自制手冲。")

# 1. 咖啡主题封面图片
st.image("https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=800", caption="精致的手冲咖啡")

# 2. 咖啡馆背景音乐
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

# 3. 在线教学视频测试
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# 4. 品牌 Logo
st.logo("🍁")

# 5. 图表
coffee = {"美式": [2, 3],
          "英式":[4, 5],
          "法式":[6, 7]}
st.table(coffee)

# 6. 输入框
coffee_name = st.text_input("请输入咖啡名：")
st.write(f"你输入的咖啡名为：{coffee_name}")

# 7.糖度输入框
coffee_sugar = st.text_input("请输入糖度：")
st.write(f"你输入的糖度为：{coffee_sugar}")

# 8. 单选按钮
coffee_type = st.radio("请选择付款方式：", ["wechat", "applepay", "card"], index=2)
st.write(f"付款方式为：{coffee_type}")