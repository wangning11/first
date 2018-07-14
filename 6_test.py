# 所谓水仙花数是指一个3位的十进制数,其各位数字的立方和恰好等于该数本身
print('水仙花数：')
number = 100
while number < 1000:
    a = number//100
    b = (number//10)%10
    c = number%10
    if number == (a**3+b**3+c**3):
        print(number)
    number += 1
