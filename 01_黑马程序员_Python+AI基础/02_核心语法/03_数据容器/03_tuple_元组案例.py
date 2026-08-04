"""
1、统计每个学生的总分、各科平均分。
2、各科成绩的最高分、最低分、平均分。
3、查找平均分 > 90的。
"""
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "王林", 85, 92, 78),
    ("S003", "王林", 99, 92, 99),
    ("S004", "王林", 85, 92, 78),
    ("S005", "王林", 97, 92, 89),
    ("S006", "王林", 99, 92, 99)
)
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")
print()
chinese_score = [s[2] for s in students]
math_score = [s[3] for s in students]
english_score = [s[4] for s in students]
print(f"语文最高分：{max(chinese_score)}, 最低分：{min(chinese_score)}, 平均分{sum(chinese_score)/len(chinese_score):.1f}")
print(f"数学最高分：{max(math_score)}, 最低分：{min(math_score)}, 平均分{sum(math_score)/len(math_score):.1f}")
print(f"英语最高分：{max(english_score)}, 最低分：{min(english_score)}, 平均分{sum(english_score)/len(english_score):.1f}")
print()
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")
