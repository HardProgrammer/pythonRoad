'''
字典：
    字典是python中唯一的映射类型，采用键值对（key-value）的形式存储。
    python对key进行哈希函数运算，根据计算的结果决定value的存储地址，所以字典是无序存储的，且key必须是可哈希的（特征：无序，键唯一）。
    可哈希表示key必须是不可变类型，如数字、字符串、元组。
    备注：可变类型指列表以及字典。
'''

# 定义一个dict，并打印输出（中文叫“字典”）
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

# 直接打印输出
print(d)

# 获取value的方法一：
print('Adam:', d['Adam'])
print('Lisa:', d['Lisa'])
print('Bart:', d['Bart'])

# 获取value的方法二
print('Adam:', d.get('Adam'))
print('Lisa:', d.get('Lisa'))
print('Bart:', d.get('Bart'))

# 添加新元素，如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value
d["lxw"] = 100
d['Lisa'] = 88
print(d)

# 遍历输出
for key in d:
    print(key + ':', d[key])

# 添加字典
d["Adams"] = 35
print("添加后的字典：", d)

# 更改某个key的value值
d["Adams"] = 66
print("更改后的字典：", d)

# 定义一个新的key值
newd = {
    'test': 234,
    'lxw': 999
}

# 更新新的字典，使用update会添加没有的键值对，如果key值存在会更改原来的value值
d.update(newd)
print("update更改后的字典：", d)

# setdefault()的用法，如果key存在不改变原来的值，如果key不存在就增加
result = d.setdefault("Adams", 111)
print("setdefault更改后的字典：", d)
print("setdefault后的返回值：", result)

# 这边会添加一个，并且会获取到添加的value值
result = d.setdefault("liuxw", 111)
print("setdefault更改后的字典：", d)
print("setdefault后的返回值：", result)

# 获取字典里的所有key值并存放到list中
list_key = dict.keys(d)
print("d字典的所有key值：", list_key)

print("d字典的所有key值：", list(dict.keys(d)))

# 获取字典里的所有value值并存放到list中
list_value = dict.values(d)
print("d字典的所有value值：", list_value)
print("d字典的所有value值：", list(dict.values(d)))

# 获取字典里的所有键值对并放到list中
list_item = dict.items(d)
print("d字典的所有键值对：", list_item)
print("d字典的所有键值对：", list(dict.items(d)))

# 删除键值对--del没有返回值
del d["liuxw"]
print("删除一个后的字典：", d)

# 删除键值对--pop有返回值value
results = d.pop("Adams")
print("pop的值：", results)
print("pop后的字典：", d)

# 随机删除一个键值对，返回键值对
ret = d.popitem()
print("随机删除后的返回值：", ret)
print("随机删除后的字典：", d)

# 清空键值对
d.clear()
print("清空后的字典：", d)

# 直接删除字典，内存释放
del d

dict_test = {'name':"11","age":12,"class":"yzd"}
# 输出字典可打印的字符串表示
print(str(dict_test))

# 输出键的总个数
print(len(dict_test))
print(dict_test.get("aa"))

key = dict_test.popitem()
print(key[0])