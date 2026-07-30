# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1、找出同时选修 法语 和 艺术 的学生。
# 方式一：
fa_set1 = french_set.intersection(art_set)
print(fa_set1)
# 方式二：
fa_set2 = french_set & art_set
print(fa_set2)
print()

# 2、同时选修四门课程的学生。
fb_set = football_set & basketball_set & french_set & art_set
print(fb_set)
print()

# 3、选修了足球，但没有选修篮球的学生。
# 方式一：
fc_set1 = football_set.difference(basketball_set)
print(fc_set1)
# 方式二：
fc_set2 = football_set - basketball_set
print(fc_set2)
# 方式三：
fc_set3 = {s for s in football_set if s not in basketball_set}
print(fc_set3)
print()

# 4、统计每一个学生选修的课程数量。
# 4.1 获取到学生名单 --并集
# all_set1 = football_set.union(basketball_set).union(french_set).union(art_set)
all_set2 = football_set | basketball_set | french_set | art_set
# print()
# 4.2 获取每一个学生选修的课程数量
all_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_list)
for s in all_set2:
    print(f"学生：{s}课程数量：{all_list.count(s)}")