print('面试资格确认:')
age = int(input('输入年龄:'))
subject = input('输入所学专业:')
college = input('是否为重点大学：')
if age > 25 and subject =='电子信息工程':
    print('录取')
elif subject =='电子信息工程' and college == '是':
    print('录取')
elif age < 28 and subject == "计算机专业":
    print('录取')
else:
    print('抱歉,您未达到面试要求')
