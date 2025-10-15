print('Hello Brother!!, v2')Hello Brother!!, v1


arr = [100,90,80,70,60,50,40,30,20,10]

def selection_sort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i, len(arr)):
            if arr[j]<arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return arr
res = selection_sort(arr)
print("before sort: ", arr)
print('after sort:', res)