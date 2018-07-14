#  求50~100之间的偶数之和并且输出
number = 50
sum = 0
while number <= 100:
    if number%2 == 0:
        sum += number
    number += 1
print('50~100之间的偶数之和:',sum)
