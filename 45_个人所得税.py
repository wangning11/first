while True:
    money = int(input("请输入金额计算个人总收入："))
    if money <= 3500:
        print('不用交税，你的个人收入是：%d'%money)
    elif money - 3500 <= 1500:
        shui = (money-3500)*0.03
        money = money-shui
        print('交税%d，你的个人收入是：%d' %(shui,money))
    elif money - 3500 <= 4500:
        shui = (money - 3500) * 0.1
        money = money - shui
        print('交税%d，你的个人收入是：%d' % (shui, money))
    elif money - 3500 <= 9000:
        shui = (money - 3500) * 0.2
        money = money - shui
        print('交税%d，你的个人收入是：%d' % (shui, money))
    elif money-3500<=35000:
        shui = (money - 3500) * 0.25
        money = money - shui
        print('交税%d，你的个人收入是：%d' % (shui, money))
    elif money - 3500 <= 55000:
        shui = (money - 3500) * 0.3
        money = money - shui
        print('交税%d，你的个人收入是：%d' % (shui, money))
    elif money-3500<=8000:
        shui = (money - 3500) * 0.35
        money = money - shui
        print('交税%d，你的个人收入是：%d' % (shui, money))
    else:
        shui = (money - 3500) * 0.45
        money = money - shui
        print('交税%d，你的个人收入是：%d' % (shui, money))
    break    
