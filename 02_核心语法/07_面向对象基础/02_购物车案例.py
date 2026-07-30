"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""

class Shop:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num
    # 魔法方法
    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"
    # 修改商品信息
    def update_shop(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

class Shopping_Cart:
    system_name = "购物车管理系统"
    def __init__(self):
        self.shopping_list = []

    # 1. 添加购物车
    def add_cart(self):
        name = input("录入商品名称：")
        # 判断商品是否存在
        for s in self.shopping_list:
            if s.name == name:
                print("已存在，不能添加")
                return

        price = float(input("录入商品价格："))
        num = int(input("录入商品数量："))
        # 添加到购物车
        sp = Shop(name, price, num)
        self.shopping_list.append(sp)

    # 2. 修改购物车
    def update_shopping(self):
        name = input("录入要修改的商品名称：")
        for s in self.shopping_list:
            if s.name == name:
                print(f"购物车信息：{s}")
                price = float(input("录入要修改的商品价格："))
                num = int(input("录入要修改的商品数量："))
                # 判断 价格和数量 是否有效
                if price >= 0 and num > 0:
                    s.update_shop(price, num)
                    print(f"修改购物车成功：{s}")
                    return

        print("未找到，修改购物车失败！")

    # 3. 删除购物车
    def delete_shopping(self):
        name = input("录入要删除的商品名称：")
        for s in self.shopping_list:
            if s.name == name:
                self.shopping_list.remove(s)
                print(f"删除购物车成功：{s}")
                return
        print("未找到，删除购物车失败！")

    # 4. 查询购物车 —— (将购物车中的商品信息展示出来)
    def query_shopping(self):
        if not self.shopping_list:
            print("购物车什么都没有")
            return

        for s in self.shopping_list:
            print(s)

    def run(self):
        print(f"{self.system_name}")

        while True:
            print("\n# 1. 添加购物车   2.修改购物车 3.删除购物车 4.查询购物车 5.退出购物车 #\n")
            choice = input("输入要执行的操作：")
            try:
                match choice:
                    case "1":
                        self.add_cart()
                    case "2":
                        self.update_shopping()
                    case "3":
                        self.delete_shopping()
                    case "4":
                        self.query_shopping()
                    case "5":
                        break
                    case _:
                        print("输入错误，重新输入")
            except Exception:
                print("程序出现错误，请重新选择")

# 测试
if __name__ == "__main__":
    s_Shopping_Cart = Shopping_Cart()
    s_Shopping_Cart.run()