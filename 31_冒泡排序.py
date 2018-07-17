arr = [4,9,2,7,1,0,3]

def buddle_sort(arr):
    n = len(arr)
    for j in range(0,n-1):
        for i in range(0,n-1-j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] =arr[i + 1], arr[i]


buddle_sort(arr)
print(arr)
