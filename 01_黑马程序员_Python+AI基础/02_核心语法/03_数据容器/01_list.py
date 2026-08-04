# # 1：将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# merge_list = list1 + list2 + list3
# print("合并后的原始列表为: ", merge_list)
# new_list = []
# for i in merge_list:
#     if i not in new_list:
#         new_list.append(i)
# new_list.sort()
# print("去重后 排序好的列表为: ",new_list)
#
# # 2. 将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表.
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# new_list = [i**2 for i in list4 if i % 3 == 0 or i % 5 == 0]
# print(new_list)

# # 3. 将如下列表中的正数提取出来，封装为一个新的列表。
# list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# new_list = [i for i in list5 if i > 0]
# print("排序好之后的：", sorted(new_list))