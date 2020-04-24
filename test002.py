def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [1,4,2,3,6,5,7]
bubbleSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])


