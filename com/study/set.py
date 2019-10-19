'''
    集合：
        不允许重复元素,随机排列
'''

# 创建set集合
list = ["aaa", "bbb", "ccc", "aaa"]

set_create = set(list)

# 打印出来后会删除相同元素,并且顺序会相反
print(set_create)

# set添加元素，并且是无序的
set_create.add("lxw")

print("添加元素后：", set_create)

# set删除元素
set_create.remove("aaa")

print("删除元素后：", set_create)

# set判断是否存在某元素，并且区分大小写
print('aaa' in set_create)
print('ccc' in set_create)

# 更新--其实就是插入一个元素，相同字符只插入一个字符
set_create.update("ee")

print('更新后的集合1', set_create)

set_create.update("abbuu")

print('更新后的集合2', set_create)

# 随机删除某个元素
set_create.pop()

print('随机删除后的集合', set_create)

# for循环遍历输出
for name in set_create:
    print(name)

# set定义对象
s1 = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])

# 遍历输出对象
for x in s1:
    print(x[0] + ':', x[1])

# 清空集合
set_create.clear()
