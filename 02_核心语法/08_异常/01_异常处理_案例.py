try:
    print("==============================")
    print(my)
    print("******************************")
except Exception as e: # 包含所有异常情况
    print("程序出现错误，错误信息：", e)
finally: # 可选
    print("完毕")