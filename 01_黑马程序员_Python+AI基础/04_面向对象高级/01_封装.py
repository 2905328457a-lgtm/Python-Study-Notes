"""
封装：将属性和方法隐藏起来，只暴露必要的属性和方法
1. 公有属性：属性名
2. 私有属性：__属性名
注意事项：Python中没有真正的私有属性
"""

# 定义手机类
class Car:
    # 初始化
    def __init__(self, brand, model, color, owner):
        self.brand = brand # 品牌(公有属性)
        self.model = model # 型号(公有属性)
        self.color = color # 颜色(公有属性)

        self.__owner = owner # 拥有者(私有属性)

    def start(self):
        print(f"{self.brand} {self.model} 启动")

    def run(self):
        print(f"{self.__owner} : {self.brand} {self.model} 行驶")
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand} {self.model} 停止")

    def __control_fuel(self):
        print(f"{self.brand} {self.model} 控制燃料")

    def get_owner(self):
        return self.__owner[0:1] + "*****"


if __name__ == '__main__':
    car = Car("宝马", "X5", "黑色", "张三")
    print(car.brand)
    print(car.model)

    print(car._Car__owner)
    car._Car__control_fuel()

    car.start()
    car.run()
    car.stop()