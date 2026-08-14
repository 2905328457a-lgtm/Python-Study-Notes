from abc import ABC, abstractmethod
import json

# 定义图书类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id              # 图书编号
        self.title = title                  # 图书名称
        self.author = author                # 作者
        self.total_num = total_num          # 总数
        self.__available_num = total_num    # 可用数量

    def borrow_book(self):   # 借书
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    def return_book(self): # 还书
        self.__available_num += 1
        return True

    def get_available_num(self): # 获取可用数量
        return self.__available_num

# 定义成员类
# 抽象类，用于定义成员的基本属性和方法 abc 模块
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id          # 成员编号
        self.name = name                    # 成员姓名
        self.__password = password          # 密码
        self.__borrow_books = []            # 借阅的图书列表

    def borrow_book(self, book):   # 借书
        # 检查是否达到最大借书数量
        if len(self.__borrow_books) >= self.get_max_borrow_books():
            print("借书失败，达到最大借书数量")
            return False

        # 检查图书是否可借
        if book.borrow_book():
            self.__borrow_books.append(book)
            print(f"{self.name} 借书成功，书名为 {book.title}")
            return True
        else:
            print(f"借书失败，图书{book.title}不可借")
            return False

    def return_book(self, book):   # 还书
        if book in self.__borrow_books:
            self.__borrow_books.remove(book)
            print(f"{self.name} 还书成功，书名为 {book.title}")
            return True
        else:
            print(f"还书失败，图书 {book.title} 不在借阅列表中")
            return False

    def get_borrow_books(self): # 获取借阅的图书列表
        return self.__borrow_books
    def get_password(self): # 获取密码
        return self.__password

    # 抽象方法(必须子类中实现)
    @abstractmethod
    def get_max_borrow_books(self) -> int: # 获取最大可借图书数量
        pass

# 普通会员类
class NormalMember(Member):
    def get_max_borrow_books(self) -> int: # 获取最大可借图书数量
        return 3

# VIP会员类
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level          # 会员等级
    def get_max_borrow_books(self) -> int:         # 获取最大可借图书数量
        return 6 + self.vip_level


# 图书管理系统类
class LibrarySystem:
    def __init__(self):
        self.books = {}                 # 图书列表
        self.members = {}               # 成员列表
        self.current_member : Member|None  = None        # 当前登录的成员
        # 加载图书和成员数据
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self): # 加载图书数据
        with open("data/books.json", "r", encoding="utf-8") as f:
            book_data = json.load(f)
            for book in book_data:
                self.books[book["编号"]] = Book(book["编号"], book["标题"], book["作者"], book["数量"])  # 创建图书对象并添加到图书列表中
            print("图书数据加载成功")  # 加载成功后打印提示信息

    def load_members_data(self): # 加载成员数据
        with open("data/members.json", "r", encoding="utf-8") as f:
            member_data = json.load(f)
            for member in member_data:
                if member["卡号"].startswith("N"):
                    self.members[member["卡号"]] = NormalMember(member["卡号"], member["姓名"], member["密码"])  # 创建普通会员对象并添加到成员列表中
                elif member["卡号"].startswith("V"):
                    self.members[member["卡号"]] = VIPMember(member["卡号"], member["姓名"], member["密码"], member["会员等级"])  # 创建VIP会员对象并添加到成员列表中
            print("成员数据加载成功")  # 加载成功后打印提示信息

    def login(self): # 登录
        while True:
            print("【登录】")
            member_id = input("请输入卡号：")
            password = input("请输入密码：")
            # 检查成员是否存在
            if member_id not in self.members:
                print("登录失败，成员不存在")
                continue
            # 检查密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                self.current_member = member
                print(f"登录成功，欢迎 {member.name} 登录")
                return True
            else:
                print("登录失败，密码错误")
                continue

    def borrow_book(self): # 借书
        # 1. 展示当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号：{book.book_id}，书名：{book.title}，作者：{book.author}，数量：{book.total_num}，可用数量：{book.get_available_num()}")

        # 2. 用户选择要借的图书
        book_id = input("【请输入要借的图书编号：】")
        if book_id not in self.books:
            print("借阅失败，图书编号不存在")
            return
        self.current_member.borrow_book(self.books[book_id])

    def return_book(self): # 还书
        # 1. 展示当前会员的借阅列表
        borrow_books = self.current_member.get_borrow_books()  # 获取当前会员的借阅列表
        print("【已经借阅的图书列表】")
        for book in borrow_books:
            print(f"编号：{book.book_id}，书名：{book.title}，作者：{book.author}")  # 展示借阅列表

        # 2. 用户选择要还的图书
        book_id = input("【请输入要还的图书编号：】")
        if book_id not in self.books:
            print("还书失败，图书编号不存在")
            return
        self.current_member.return_book(self.books[book_id])

    def show_borrow_books(self): # 查看借阅列表
        borrow_books = self.current_member.get_borrow_books()  # 获取当前会员的借阅列表
        if len(borrow_books) > 0:
            print("【已经借阅的图书列表】")  # 展示借阅列表
            for book in borrow_books:
                print(f"编号：{book.book_id}，书名：{book.title}，作者：{book.author}")  # 展示借阅列表
        else:
            print("当前会员没有借阅任何图书")

    def run(self):
        if self.login():
            while True:
                print("【图书管理系统】")
                print("1. 借书")
                print("2. 还书")
                print("3. 查看借阅列表")
                print("4. 退出")
                choice = input("请输入选项：1-4：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrow_books()
                    case "4":
                        print("退出系统")
                        break
                    case _:
                        print("无效选项，请重新输入")


if __name__ == '__main__':
    s = LibrarySystem()
    s.run()  # 运行图书管理系统
