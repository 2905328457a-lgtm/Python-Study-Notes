"""
重写：子类重写父类的方法，实现方法的重写。
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

    def __control_fuel(self): # 私有方法
        print(f"{self.brand} {self.model} 控制油门")

    def get_owner(self):
        return self.__owner[:1] + "**"

    def charge(self):
        print(f"{self.brand} {self.model} 正在充电")

# 继承
class FuelCar(Car): # 燃油车
    # 重写方法
    def charge(self):
        # 方式一: 调用父类方法 super().方法名()
        # super().charge()
        # print(f"{self.brand} {self.model} 正在加油…………")

        # 方式二: 类名.方法名(self)
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在加油……")


class ElectricCar(Car):  # 电车
    # 重写方法
    def charge(self):
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在充电中……")


if __name__ == '__main__':
    c1 = FuelCar("特斯拉", "Model S", "白色", "张三")
    c2 = ElectricCar("特斯拉", "Model X", "黑色", "李四")
    c1.charge()
    c2.charge()

