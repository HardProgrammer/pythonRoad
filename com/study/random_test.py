# 随机数
import random
# 字符串
import string

# 产生0-10内的浮点数
print(random.random())

# 产生0-10内的整数
print(random.randint(0,10))

# 从a-zA-Z0-9生成指定数量的随机字符：
str_ran = ''.join(random.sample(string.ascii_lowercase + string.digits,8))
print(str_ran)

# 从字符串中获取随机字符
print(random.choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-="))