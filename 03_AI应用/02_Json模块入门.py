import json

# # 写入json文件
# user = {
#     "name": "张三",
#     "age": 18,
#     "gender": "男",
#     "hobby": ["看电影", "听音乐", "看小说"],
#     "address": {
#         "province": "北京",
#         "city": "北京"
#     }
# }
# with open("resources/user.json", 'w', encoding="utf-8") as f:
#     json.dump(user, f, ensure_ascii=False, indent=4)


# 读取json文件
with open("resources/user.json", 'r', encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))