'''
实现购物车逻辑：
    通过现有的金额去对比商品价格，判断余额是否足够，并且添加到相应的购物车数组中
'''

# 定一个商品以及商品价格
product_list = [
    ('Mac', 9000),
    ('kindle', 800),
    ('tesla', 9000),
    ('python book', 105),
    ('bike', 2000),
]

# 输入所拥有的金额
money = input('please input your money:')
shopping_car = []
# 判断是否数字
if money.isdigit():
    # 转换为int类型
    money = int(money)
    while True:
        # 打印出商品内容(这里1代表索引从1开始)
        for i, v in enumerate(product_list, 1):
            print(i, '>>>>', v)
        choice = input('选择购买商品编号[退出：q]：')
        # 判断是否为数字，如果是q就结算，不是就转换
        if choice.isdigit():
            choice = int(choice)
            # 判断序号是都溢出或者小于0
            if choice > 0 and choice <= len(product_list):
                # 获取对应序号的商品
                p_item = product_list[choice - 1]

                # 如果钱够，用本金减去该商品价格，并将该商品加入购物车
                if p_item[1] < money:
                    money -= p_item[1]
                    # 将商品加入到购物车列表
                    shopping_car.append(p_item)
                # 金额不足提示
                else:
                    print('余额不足，还剩%s' % money)
                # 输出选择的商品
                print(p_item)
            else:
                print('编码不存在')
        elif choice == 'q':
            print('------------您已经购买如下商品----------------')
            # 循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱' % money)
            break
        else:
            print('invalid input')
