#insertionSort
arr = [8, 3, 6, 2, 4, 1, 7, 5]
def insertSort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(insertSort(arr))

