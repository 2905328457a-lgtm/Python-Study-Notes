"""
多态：在继承关系中，子类可以重写父类的方法，使得子类的方法具有不同的实现方式。
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


    def stop(self):
        print(f"{self.brand} {self.model} 停止行驶")

    def __control_fuel(self): # 私有方法
        print(f"{self.brand} {self.model} 控制油门")

    def get_owner(self):
        return self.__owner[:1] + "**"

    def charge(self):
        print(f"{self.brand} {self.model} 正在充电")

class FuelCar(Car): # 燃油车
    # 重写方法
    def charge(self):
        print(f"{self.brand} {self.model} 正在加油中……")

class ElectricCar(Car):  # 电车
    # 重写方法
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电中……")

# 封装燃料函数
def handle_charge(car: Car):
    car.charge()


if __name__ == '__main__':
    handle_charge(FuelCar("比亚迪", "宋", "蓝色", "王五"))
    handle_charge(ElectricCar("特斯拉", "Model X", "黑色", "李四"))

