"""需求1：定义一个函数，根据传入的分数，计算对应的分数等级并返回。
- 分数 >= 90：A
- 分数 >= 75：B
- 分数 >= 60：C
- 分数 < 60：D
"""
def scores(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
print(scores(90))
print(scores(70))
print(scores(60))

"""需求2：定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
"""
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))

"""需求3：定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。"""
def time_conversion(total_seconds):
    """
    算小时：1 小时 = 3600 秒。3661//3600=1小时（拿整数部分）。
        剩下多少秒？3661%3600=61秒。
    算分钟：1 分钟 = 60 秒。
        拿剩下的 61//60=1分钟。
    算秒数：
        拿剩下的 61%60=1秒。
    :param seconds: 传入的秒数
    :return: 转换后的小时、分钟、秒
    """
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 3600) % 60
    return f"{total_seconds}转换后：{hours}小时:{minutes}分钟:{seconds}秒"
print(time_conversion(3772))

"""需求4：定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。"""
def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "等边三角形"
        elif a == b or b == c or c == a:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"
print(triangle_type(1, 2, 1))