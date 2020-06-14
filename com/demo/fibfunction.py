'''
 斐波那数列   
    1,1,2,3,5,8,13,21,34...
'''
import time

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return "done"

fib(10) 

# 生成器--解决如果max过大会导致卡顿问题
def fib_list(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 转化成生成器
        yield b
        a,b = b,a+b
        n += 1
    # 用语异常打印效果
    return "done"

f = fib_list(100)

# 唤醒
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

# 生成器的运用
def consumer(name):
    print(name + "准备...")
    while True:
        baozi = yield
        print(name + "吃包子")

def producer(name):
    c = consumer("A")
    cx = consumer("B")
    c.__next__()
    cx.__next__()
    print("开始测试")
    for i in range(10):
        time.sleep(1)
        print("测试执行")
        c.send(i)
        cx.send(i)


producer("lxw")