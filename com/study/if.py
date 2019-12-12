'''
循环语句：
    有限循环，代表次数有限制
    无限循环=死循环，代表次数没有限制
    continue 结束本次循环，继续下一次循环
    break 跳出整个当前的循环
'''

# if语句进行判断输出
a = 1
n = 2
if a > n:
    print(a)
else:
    print(n)

# 多重判断
score = 85
if score >= 90:
    print('excellent')
    print("Ok")
elif score >= 80:
    print('good')
    # 这边会继续输出
    print("JUST SO SO")
elif score >= 60:
    print('passed')
else:
    print('failed')

# bool变量，一般用于设置标识符
flag = False

if not flag:
    print("你好啊！")
