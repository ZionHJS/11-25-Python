#python swap
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]

#bubble sort
arr = [8,3,6,2,4,1,7,5]
def bubble(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    bubble(arr)
    print(arr)
bubble(arr)