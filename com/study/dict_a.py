'''
    字典的操作:
        创建、查询、更新
'''

# fromkeys创建字典--使用不同的key对应相同的一个value值
d = dict.fromkeys(['host1', 'host2', 'host3'], 'test')
print(d)

d1 = dict.fromkeys(['host1', 'host2', 'host3'], ['test1', 'test2'])
print(d1)

# 更换value为list的数值--前面一个key值为任意一个
d1['host1'][1] = "test3"
print("更换后的字典值", d1)

# 更新key值为host1的value值
d1['host1'] = "test"
print("更换后的字典值", d1)

# 多级字典
most_dict = {
    "福建": {
        "厦门": ["有思明区和湖里区"],
        "泉州": ["不错的城市"],
        "福州": ["四大火炉之一"]
    },
    "江西": {
        "南昌": ["省会"]
    }
}
print(most_dict)

# 更新某个数据
most_dict["福建"]["厦门"][0] = "压力山大"
print("更新后的字典：", most_dict)

dic = {5: '555', 2: '666', 4: '444'}
# 判断主键是否存在
print(5 in dic)             # True存在
print(6 in dic)             # False不存在

# 排序操作--根据键值进行排序并打印全部数据
print(sorted(dic.items()))

# 排序操作--根据键值进行排序并打印key值
print(sorted(dic.keys()))

# 排序操作--根据value值进行排序并打印value值
print(sorted(dic.values()))

dict_obj = {'name': 'alex', 'age': 18}

# 字典的遍历--i代表key值
for i in dict_obj:
    print(i, ":", dict_obj[i])

# 字典的遍历2--i代表key值
for i, v in dict_obj.items():
    print(i, ":", v)
