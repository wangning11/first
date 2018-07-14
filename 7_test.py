# 求200以内能被17整除的最大整数
print('200以内能被17整除的最大整数:')
number = 200
while number > 0:
    if number%17 == 0:
        print(number)
        break
    number -= 1
