str = input('请输入一窜字符：')
resoult = {}
for i in str:
    resoult[i] = str.count(i)
print(resoult)
