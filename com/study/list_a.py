list_test = ["aaa", "aaa", "eee", "bbb", "ccc", "ddd"]

print("排序前的数据：", list_test)

# 反转
list_test.reverse()
print("反转后的数据：", list_test)

# 排序
list_test.sort()
print("排序后的数据：", list_test)

# 获取list的总个数
print(len(list_test))

# 获取list中某元素的个数
print(list_test.count("aaa"))

# 列表的拼接
list_two = ["eee", "fff"]
list_two.extend(list_test)

print("拼接后的数据：", list_two)
# 后面的数据不变
print("被拼接的数据：", list_test)

# 获取某字符串在列表中的位置，相同的情况下取第一个的位置
print(list_test.index("ccc"))

# 测试赋值
a,b = [2,3]
# a的值为2
print(a)  
# b的值为3          
print(b)

list_a = [2,3,4,5,6,7]

if a in list_a:
    print("a在list_a中")

# 返回列表元素中的最大值
print(max(list_a))

# 返回列表元素中的最小值
print(min(list_a))