people1 = '你知道我生日吗？'
people2 = '输入你的身份证号码'
people3 = '123456199601012223'

year = people3[11:15]
month = people3[15:17]
day = people3[17:19]
print(people1+'\n'+people2+'\n'+people3)
print('程序员乙：你是%s年%s月%s日出生的，所以你的生日是%s月%s日'%(year,month,day,month,day))
