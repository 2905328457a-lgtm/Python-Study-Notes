"""
多继承：一个子类继承多个父类，子类可以继承多个父类的属性和方法。
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

# 华为智驾
class HuaweiAiDriver:
    def __init__(self, version = 1.0):
        self.version = version
    def run(self):
        print(f"华为智驾版本 {self.version} 正在运行")

# 特斯拉
class TeslaAiDriver(Car, HuaweiAiDriver):
    def __init__(self, bread, model, color, owner, version = 1.0):
        # super().__init__(bread, model, color, owner)
        Car.__init__(self, bread, model, color, owner)
        HuaweiAiDriver.__init__(self, version)
    # 重写父类方法
    def run(self):
        # Car.run(self)
        HuaweiAiDriver.run(self)


# MRO: Method Resolution Order(方法解析顺序) → 类名.mro()
if __name__ == '__main__':
    c1 = TeslaAiDriver("特斯拉", "Model S", "白色", "张三", 1.1)
    print(c1.__dict__)
    c1.run()

