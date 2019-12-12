'''
    实现一个登陆逻辑--最简单判断
'''

userName = input("请输入账号：")
print(userName)

password = input("请输入密码：")
print(password)

if userName == "admin" and password == "123":
    print("登陆成功")
elif userName != "admin":
    print("账号错误")
elif password != "123":
    print("密码错误")
