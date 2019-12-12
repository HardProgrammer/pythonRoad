'''
while 表达式：
    当表达式为true的时候继续执行
else:
    当没有执行break语句并且while后面表达式不成立时，会执行else语句
break 终止循环操作
'''
# 输出0-100的偶数
even_numbers = 1
while even_numbers <= 100:
    # 偶数除2取余为0，奇数为1
    if even_numbers % 2 == 0:
        print(even_numbers)
    even_numbers += 1

# while语句实现0-100相加
num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
print(sum)

# while的嵌套--实现倒序
line = 5
while line > 0:
    temp = line
    while temp > 0:
        print("*",end="")
        temp -= 1
    print()
    line -= 1

# while的嵌套--实现正序
line_number = 1
while line_number < 5:
    temp_number = 1
    while temp_number <= line_number:
        print("*",end="")
        temp_number += 1
    print()
    line_number += 1

# 实例：根据输入猜测变量
age = 30
login_number = 1
while login_number <= 5:
    user_age = int(input("input your age :"))
    if user_age < age:
        print("Too small")
    if user_age == age:
        print("you are right")
        break
    if user_age > age:
        print("Too big")
    login_number += 1
# 当没有执行break语句并且while后面表达式不成立时，会执行else语句
else:
    print("end")