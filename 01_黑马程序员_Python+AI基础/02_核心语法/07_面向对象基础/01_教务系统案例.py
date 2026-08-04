"""
采用面向对象的编程思想，开发一个教务管理系统，实现学员成绩信息的添加、修改、删除、查询与展示功能。系统使用自定义对象存储学员数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加学生成绩：用户根据提示录入学生姓名、语文成绩、数学成绩、英语成绩，保存该学生信息到教务系统中（成绩需在 0~100 分之间，同名学员不可重复添加）。
    2. 修改学生成绩：要求用户输入要修改的学生姓名，然后再提示输入修改后的语文、数学、英语成绩，输入完成后更新该学员的成绩信息。
    3. 删除学生成绩：要求用户输入要删除的学生姓名，根据姓名从教务系统中删除该学员信息。
    4. 查询指定学生成绩：要求用户输入要查询的学生姓名，根据姓名查找并展示该学员的各科成绩及总分信息。
    5. 展示全部学生成绩：将教务系统中的所有学员成绩展示出来，格式为："姓名：xxx | 语文：xxx | 数学：xxx | 英语：xxx | 总分：xxx"。
    6. 退出教务程序：退出教务管理系统，结束程序运行。
"""
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    # 魔法方法 -str
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    # 修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"
    def __init__(self):
        self.student_list = []
    # 添加学生成绩
    def add_student(self):
        name = input("输入学生姓名：")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print("已存在 不能添加")
                return

        chinese = int(input("输入学生语文成绩："))
        math = int(input("输入学生数学成绩："))
        english = int(input("输入学生英语成绩："))

        # 验证成绩范围 (0~100)
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("学生成绩添加成功")
        else:
            print("各科成绩必须得在0~100中")
    # 修改学生成绩
    def update_student(self):
        name = input("输入要修改的学生姓名：")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")

                chinese = int(input("输入修改后的语文成绩："))
                math = int(input("输入修改后的数学成绩："))
                english = int(input("输入修改后的英语成绩："))

                # 验证成绩范围 (0~100)
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("各科成绩必须得在0~100中")
                    return
        print("未找到该学生，修改失败！")

    # 删除学生成绩
    def delete_student(self):
        name = input("输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print(f"已删除{s}学生")
                return
        print("未找到该学生，删除失败！")

    # 查询指定学生成绩
    def query_student(self):
        name = input("输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生，查询失败！")

    # 展示全部学生成绩
    def list_student(self):
        if not self.student_list:
            print("当前系统中暂无学员成绩信息")
            return
        for s in self.student_list:
            print(s)

    # 运行程序
    def run(self):
        print(f"欢迎使用教务管理系统 V{self.system_version}")

        while True:
            print("1.添加学生成绩 2.修改学生成绩    3.删除学生成绩    4.查询指定学生成绩  5.展示全部学生成绩 6.退出程序")
            print()
            choice = input("输入执行的操作：")
            # 捕获异常
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("Bye~")
                        break
                    case _:
                        print("重新输入")
            except Exception as e:
                print("程序出现错误，错误信息：", e)

# 测试
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()