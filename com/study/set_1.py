'''
    set：无序的，去重
    set的比较，包含，交集，并集，差集
'''

# set比较是否相等
print(set("aaabbb") == set("ab"))

# 去重
name_x = set(["测试","xx","aa","xx"])
print("name_x:", name_x)

name_a = set([1, 2, 9, 4, 5, 6])

name_b = set([1, 2, 44, 11, 22, 6])

print("name_a:", name_a)

# 交集
print(name_a.intersection(name_b))
print("交集:", name_a & name_b)

# 并集
print(name_a.union(name_b))
print("并集:", name_a | name_b)

# 差集--取a有的b没有集合
print(name_a.difference(name_b))
print("差集:", name_a - name_b)

# 差集--取b有的a没有集合
print(name_b.difference(name_a))
print("差集:", name_b - name_a)

# 取交集之外的并集--对称差集
print(name_a.symmetric_difference(name_b))
print("对称差集:", name_a ^ name_b)

# 父级--超集（判断前面的集合是否在后面的之内--注意set是不可重复的）
print(name_a > name_b)
print(name_a.issuperset(name_b))

# 子集
print(name_a.issubset(name_b))
print(name_a < name_b)
