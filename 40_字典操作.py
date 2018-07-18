d = {'a':1,'b':2,'c':3}
d_add = {'d':4}

print('old:')
for k in d :
    print('%s,%d'%(k,d[k]))
d.update(d_add)
print('new')
for k in d:
    print('%s,%d'%(k,d[k]))
