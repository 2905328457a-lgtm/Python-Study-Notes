"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""
menu = """   
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用教务管理系统 ~")
student = {}

while True:
    print(menu)
    choice = input("执行的操作：")
    match choice:
        case "1": # 1.添加学生信息
            student_name = input("输入学生姓名：")
            chinese_score = int(input("输入语文成绩："))
            math_score = int(input("输入数学成绩："))
            english_score = int(input("输入英语成绩："))

            if student_name in student:
                print("学生已存在")
            else:
                student[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
                print("学生信息添加完毕")
        case "2": # 2.修改学生信息
            student_name = input("输入学生姓名：")
            if student_name not in student:
                print("学生不存在")
                continue
            else:
                chinese_score = int(input("输入语文成绩："))
                math_score = int(input("输入数学成绩："))
                english_score = int(input("输入英语成绩："))
                student[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
                print("学生信息修改完毕")
        case "3": # 3.删除学生信息
                student_name = input("输入学生姓名：")
                if student_name not in student:
                    print("学生不存在")
                    continue
                else:
                    del student[student_name]
                    print("学生信息删除完毕")
        case "4": # 4.查询学生信息
                student_name = input("输入学生姓名：")
                if student_name not in student:
                    print("学生信息不存在")
                    continue
                else:
                    student_info = student[student_name]
                    print(f"学生信息{student_name}, 语文成绩：{student_info['chinese']}, 数学成绩：{student_info['math']}, 英语成绩：{student_info['english']}")
        case "5": # 5.列出所有学生
            for student_name in student.keys():
                student_info = student[student_name]
                print(
                    f"学生信息{student_name}, 语文成绩：{student_info['chinese']}, 数学成绩：{student_info['math']}, 英语成绩：{student_info['english']}")
        case "6": # 6.统计班级成绩
            if not student:
                print("系统中暂无学生信息，请先添加学生 ~")
                continue
            chinese_scores = []
            math_scores = []
            english_scores = []
            for student_name, scores in student.items():
                chinese_scores.append(scores['chinese'])
                math_scores.append(scores['math'])
                english_scores.append(scores['english'])
            # 最高分 最低分 平均分
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores)/len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores)/len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores)/len(english_scores)

            # 找出最高分和最低分的学生
            chinese_max_student = [name for name, scores in student.items() if scores['chinese'] == chinese_max]
            chinese_min_student = [name for name, scores in student.items() if scores['chinese'] == chinese_min]

            math_max_student = [name for name, scores in student.items() if scores['math'] == math_max]
            math_min_student = [name for name, scores in student.items() if scores['math'] == math_min]

            english_max_student = [name for name, scores in student.items() if scores['english'] == english_max]
            english_min_student = [name for name, scores in student.items() if scores['english'] == english_min]

            # 输出统计结果
            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_student}")
            print(f"     最低分学生: {chinese_min_student}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_student}")
            print(f"     最低分学生: {math_min_student}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_student}")
            print(f"     最低分学生: {english_min_student}")
            print("========================")

        case "7": # 7.退出系统
            print("bye~~")
            break
        case _:
            print("非法操作，不支持")