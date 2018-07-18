str_a = 'I,love,python'
str_b = 'aabbccddee'
b1 = 'ff'
b2 = b1.replace('dd','ff',1)
str_c = 'ab2b3n5nn2n67mm4n2'
print(str_a[2:6])
print(b2)
print(str_c.count('n'))
str_d = {}
for i in str_c:
    str_d[i] = str_c.count(i)
print(str_d)
