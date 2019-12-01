# python swap
arr = [1, 3, 5, 7]
arr[0], arr[1] = arr[1], arr[0]

# bubble sort
arr = [8, 3, 6, 2, 4, 1, 7, 5]


def bubbleSort(arr):
    for j in range(len(arr)):
        for i in range(1, len(arr)-j):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


print(bubbleSort(arr))


# selection sort
arr = [8, 3, 6, 2, 4, 1, 7, 5]

def selectionSort(arr):
    for j in range(len(arr)):
        min = j
        for i in range(j, len(arr)):
            if arr[min] > arr[i]:
                min = i
        arr[j], arr[min] = arr[min], arr[j]
    return arr
print(selectionSort(arr))

