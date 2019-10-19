import math
import cmath

math_list = dir(math)
cmath_list = dir(cmath)
# 获取math下的所有方法
print(math_list)
# 获取cmath下的所有方法
print(cmath_list)
# 获取数的最大值
print(max(1,3,4,2,8,7,6))
# 获取数的最小值
print(min(12,3,4,5,6,13,1,1))
# 获取数的小数和整数部分
print(math.modf(1.11))