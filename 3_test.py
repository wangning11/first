while True:
    u = 1
    user =int( input('请输入0～100的任意数字：'))
    if user == 0:
        continue
    elif user < 100:
        while u <= user:
            print('命运给予我们的不是失望之酒,而是机会之杯  %d' %u)
            u += 1
    elif user == 100:
        print('已退出')
        break
    else:
        print('请从新输入')
             
