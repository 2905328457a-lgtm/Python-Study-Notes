# # 1.打开文件
# f = open("resources/将进酒.txt", 'r', encoding="utf-8")
#
# # 2.读取文件内容
# content = f.read()
# print(content)
# # 2.1 按行读取
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip())
#
# # 3.关闭文件
# f.close()

# ---------------释放资源(方式一)-----------------------
# 写文件
# 1.打开文件
f = open("resources/春晓.txt", 'w', encoding="utf-8")
try:
    # 2.写入内容
    f.write("春晓\n\n")
    f.write("花有重开日，\n")
    f.write("春风不长，\n")
    f.write("人已老去，\n")
    f.write("风已吹散。\n")
finally:
    # 3.关闭文件
    print("文件已关闭")
    f.close()

# ---------------释放资源(方式二)——自动关闭-----------------------
# 写文件
# 1.打开文件
with open("resources/春晓.txt", 'w', encoding="utf-8") as f:
    # 2.写入内容
    f.write("春晓\n\n")
    f.write("花有重开日，\n")
    f.write("春风不长，\n")
    f.write("人已老去，\n")
    f.write("风已吹散。\n")
