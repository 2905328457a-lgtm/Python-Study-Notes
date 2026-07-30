"""
需求：用户名密码登录，正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666, 5次登录机会，输入错误五次，不允许再操作了。
"""
for i in range(5):
    username = input("输入用户名：")
    password = input("输入密码：")
    if username == "" or password == "":
        print("不能为空")
        continue
    if username == "admin" and password == "666888":
        print("登录成功！")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功！")
        break
    elif username == "taoge" and password == "888666":
            print("登录成功！")
            break
    else:
        print("登录失败")
        if i == 4:
            print("输入错误五次，不允许再登录了")
            break

