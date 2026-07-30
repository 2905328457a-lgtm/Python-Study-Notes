# 异常传递
def fun1():
    print("---------------")
    fun2()
def fun2():
    print("+++++++++++++++")
    fun3()
def fun3():
    print("///////////////")
    # fun4()
    print(my)

# 测试
if __name__ == "__main__":
    # 捕获异常
    try:
        fun1()
    except Exception as e:
        print("程序出现错误，错误信息：", e)