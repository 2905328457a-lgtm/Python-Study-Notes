# # 九九乘法表
# for i in range(1, 10): # 行
#     for j in range(1, i+1): # 列
#         print(f"{j} * {i} = {j * i}", end="\t")
#     print()

# # 等腰直角三角形
# for i in range(1, 6):
#     for j in range(1 , i+1):
#         print("*", end="\t")
#     print()

# # 数字金字塔
# for i in range(1, 7):
#     for j in range(1, i+1):
#         print(j, end="\t")
#     print()

# # 国际象棋棋盘
# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("●", end="\t")
#         else:
#             print("○", end="\t")
#     print()