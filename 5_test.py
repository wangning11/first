#求1~100之间能被7整除，但是同时不能被5整除的所有整数
print('1~100之间能被7整除，但是同时不能被5整除的所有整数:')
digital = 1
while digital <= 100:
    if digital%7 == 0 and not digital%5 == 0:
        print (digital)
    digital += 1
