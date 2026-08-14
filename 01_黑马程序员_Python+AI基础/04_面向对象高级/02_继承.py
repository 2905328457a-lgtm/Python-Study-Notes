"""
继承：子类继承父类的属性和方法
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
        print(f"{self.__owner} : {self.brand} {self.model} 正在行驶")
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand} {self.model} 停止行驶")

    def __control_fuel(self):
        print(f"{self.brand} {self.model} 控制油门")

    def get_owner(self):
        return self.__owner[:1] + "**"

# 继承
# 燃油车
class FuelCar(Car):
    pass
# 电车
class ElectricCar(Car):
    pass


if __name__ == '__main__':
    c1 = FuelCar("特斯拉", "Model S", "白色", "张三")
    c1.start()
    c1.run()
    c1.stop()

    print(c1.brand)
    print(c1.model)
    print(c1.color)
    print(c1.get_owner())



