while True:
    print('------跳一跳，输入‘退出’即可退出游------')
    print('欢迎回来，请开始游戏')
    print('请输入\（中心、音乐模块、微信支付模块）')
    player = input('请输入：')
    if player == '中心':
        print('您的分数：32')
    elif player == '音乐模块':
        print('您的分数：30')
    elif player == '微信支付模块':
        print('您的分数：42')
    elif player == '退出':
        print('已退出')
        break
    else:
        print('输入错误，请从新输入')
    
