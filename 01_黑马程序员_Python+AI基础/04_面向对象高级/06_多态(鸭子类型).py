"""
多继承：一个子类继承多个父类，子类可以继承多个父类的属性和方法。
"""

# 定义手机类
class Duck:
    def __init__(self, age, name):
        self.age = age
        self.name = "鸭子"
    def swimming(self):
        print(f"{self.age} 岁的 {self.name} 正在游泳")
class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = "狗"
    def swimming(self):
        print(f"{self.age} 岁的 {self.name} 正在游泳")

class Cat:
    def __init__(self, age, name):
        self.age = age
        self.name = "猫"
    def swimming(self):
        print(f"{self.age} 岁的 {self.name} 正在游泳")

def go_swimming(duck):
    duck.swimming()

if __name__ == '__main__':
    go_swimming(Duck(3, "小鸭子"))
    go_swimming(Dog(2, "小黑狗"))
    go_swimming(Cat(1, "小花猫"))

