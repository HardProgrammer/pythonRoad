'''
   直接赋值：其实就是对象的引用（别名）。
         a = b,赋值引用，a 和 b 都指向同一个对象。
   浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。（只拷贝第一层）
        b = a.copy() 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
   深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。（克隆）
        b = copy.deepcopy(a) 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
'''
import copy

str1 = ["11", "22", "33", [1, 3]]
# 浅拷贝：拷贝str1到str2
str2 = str1.copy()

print("str1", str1)
print("str2", str2)

# 复制是否同一个地址--不是同一个地址
print(id(str1) == id(str2))

# 更改列表的里面的列表会改变str1，如果只是单纯更改str1[0]，str2不会更改
str1[3][0] = "test"

print(str1)

# str2会等于str1
print(str2)

# 深拷贝
str3 = copy.deepcopy(str1)

str3[2] = "hello"
print("str1", str1)
print("str3", str3)
