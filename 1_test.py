'''
1 行走捐 200
2 生活缴费 300
3 共享单车 350
4 线下支付 380
5 网络购票 500
'''
while True:
    print('----------------------------------------')
    print('能量来源如下：')
    print('0 退出、 1 行走捐、2 生活缴费、3 共享单车、4 线下支付、5 网络购票')
    energy = input('查询能量请输入能量来源！退出程序请输入:')
    if energy == '0' or energy == '退出':
        print('已退出')
        break
    elif energy == '1' or energy == '行走捐':
        print('200')
    elif energy == '2' or energy == '生活缴费':
        print('300')
    elif energy == '3' or energy =='共享单车':
        print('350')
    elif energy == '4' or energy == '下线支付':
        print('380')
    elif energy == '5' or energy == '网络购票':
        print('500')
      
            
    else:
        print('输入错误，请从新输入')
        
   
