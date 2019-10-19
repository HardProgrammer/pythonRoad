'''
    递归函数实现汉诺塔
'''

# 定义一个递归函数
def move(n, a, b, c):
    # 当n=1的时候只要一步，就可以完成
    if n == 1:
        print(a, '-->', c)
        return
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)

# 汉诺塔实现
move(4, 'A', 'B', 'C')