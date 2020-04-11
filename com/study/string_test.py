'''
 字符串相关操作：
    关键字in：判断某个字符或字符串是否在字符串中；
    拼接字符串：join的效率比+ 高
'''

myStr = "测试"

print(myStr)

# 编码格式
print(myStr.encode("utf-8"))

# 编码后解码
print(myStr.encode("utf-8").decode("utf-8"))


# 创建一个字符串
str1 = "name is llnxw"
str2 = "this is string"

# 格式化输出字符串
print("%s 测试" % str1)

# 重复输出
print(str1 * 2)

# 字符串切片操作--表示从第三个字符开始到结束
print(str1[2:])

# 判断某个字符或字符串是否在字符串中
print("l" in str1)  # True 存在
print("name" in str2)  # False 不存在

# 字符串拼接
print(str1 + str2)

# 拼接列表数据，列表中的数据拼接第一个字符串
print("----".join([str1, str2, "333"]))

# string内置方法
print(str1.count("n"))  # 统计字符串中某个字符的个数

print(str1.capitalize())  # 首字母大写输出字符串

print(str1.center(20, "-"))  # 字符串居中，并且首尾添加“-”补充至20个字符
print(str1.center(10, "-"))  # 字符串居中，不足个数不进行补充
print(str1.startswith("n"))  # 判断是否以某个字符或者字符串开头
print(str1.endswith("y"))  # 判断是否以某个字符或者字符串结尾

# \打印特殊字符
str3 = "test \t \"\" hello"
# 自定义\t的个数
print(str3.expandtabs(tabsize=20))

# 查找某个字符的索引位置--默认查询第一个元素的索引值
print(str3.find("h"))

# 查找某个字符的索引位置--从右往左查，同理lfind从左往右查
print(str3.rfind("h"))

# 赋值操作--使用｛｝获取变量的值，如果没有赋值直接打印｛内容｝
str4 = "hello {name}，age {age}"
print(str4)
# 利用format将变量的值赋值给str4
# print(str4.format(name="lxw"))
print(str4.format(name="lxw", age="25"))

# 使用字典方式去赋值
print(str4.format_map({"name": "test", "age": 22}))

# 获取某个字符的索引位置--如果不存在就会报错
print(str4.index("h"))

# 判断某个字符串是否是数字或者字母
print("abc123".isalnum())  # True
print("a#".isalnum())  # False

# 判断是否十进制的数字
print("123".isdecimal())  # True
print("AF00".isdecimal())  # False
print("0.01".isdecimal())  # False

# 判断是否整型
print("990".isdigit())  # True
print("990.00".isdigit())  # False

# 判断是否纯字母
print("abv".isalpha())  # True
print("2432av".isalpha())  # False

# 检测字符串是否只由数字组成
print("abv".isnumeric())  # False
print("123.1234".isnumeric())  # False
print("123234".isnumeric())  # True

# 检测字符串是否非法变量
print("abv".isidentifier())  # True
print("123abv".isidentifier())  # False

# 检测字符串是否全部小写，isupper判断是否全是大写
print("1Abv".islower())  # False
print("abv".isidentifier())  # True

# 判断一个字符串中的字符串是否首字母大写（类似英文写法的标题首字母是否大写）
print("My Love".istitle())  # True

# 字符串大写变小写，upper小写变大写
print("My Love".lower())
print("My Love".upper())

# 字符串中大写变成小写，小写变成大写
print("My Love".swapcase())

# 右边添加字符串个数,总字符个数为10个
print("My Love".ljust(10, "*"))

# 左边添加字符串个数,总字符个数为10个
print("My Love".rjust(10, "*"))

# 去除左右两边的空格以及换行符
print("   My Love  ".strip())
print("   My Love  \ntest  ".strip())

# 去除最左边的空格以及换行符
print("   My Love  ".lstrip())
# 去除最右的空格以及换行符
print("   My Love  ".rstrip())

# 替换某个字符串, 后面可加次数（替换不超过 max 次）
print("   My Love  ".replace("ov", "l"))

# 根据某个字符进行分割成列表
print("   My Love  ".split(" "))

