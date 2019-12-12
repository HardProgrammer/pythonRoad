'''
变量（Variables）
    概念：为了存储程序运算过程中的一些中间结果，为了方便日后调用的值。变量名区分大小写。
命名规则：
    1. 要具有描述性；
	2. 变量名只能_,数字，字母组成，不可以是空格或特殊字符(#?<.，￥$*!~)；
	3. 不能以中文为变量名；
	4. 不能以数字开头；
	5. 保留字符是不能被使用；
常量
    概念：不变的量。
注意：在python中所有的变量都是可变的,所以用全部大写的变量名来代表该变量为常量。
'''
import keyword

# 输出关键字（保留字）
print(keyword.kwlist)

# 变量的用法
name ="test"
other_name = name

print("name = ",name)

other_name = "test hello"

# 赋值新的值给该变量
print("other_name = ",other_name)
# 还是原来的值
print("name = ",name)   

# 手动删除变量的值
del name
# 删除了name变量的值后输出报错--无定义
'''测试注释 (多行注释)'''
'''print(name)'''

a = b = c = 1
print("a=",a,",b=",b,",c=",c)

# 返回复数 (4+3j)
print(complex(4,3))
