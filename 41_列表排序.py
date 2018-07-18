L = [2,5,3,8,10,1]

def buddle_sort(L):
    n = len(L)
    for j in range(0,n-1):
        for i in range(0,n-1-j):
            if L[i] > L[i + 1]:
                L[i],L[i + 1] = L[i + 1],L[i]


buddle_sort(L)
print(L)
