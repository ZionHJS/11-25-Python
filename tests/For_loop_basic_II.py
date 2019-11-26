# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for x in range(0, len(list)):
        if list[x] > 0:
            list[x] = "big"
    print(list)
    return list
biggie_size([-1, 3, 5, -5])

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(list):
    count = 0
    for x in range(0, len(list)):
        if list[x] > 0:
            count = count + 1
    list[-1] = count
    print(list)
count_positives([1,6,-4,-2,-7,-2])

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(list):
    sum = 0
    for x in range(0, len(list)):
        sum = sum + list[x]
    print(sum)
sum_total([6,3,-2])

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for x in range(0, len(list)):
        sum = sum + list[x]
    average = sum/len(list)
    print(average)
average([1,2,3,4])

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(list):
    print(len(list))
length([37,2,1,-9])

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(list):
    if len(list) === 0:
        return false
    min = list[0]
    for x in range(0, len(list)):
        if list[x] < min:
            min = list[x]
    print(min)
minimum([37,2,1,-9])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(list):
    if len(list) == 0:
        return false
    max = list[0]
    for x in range(0, len(list)):
        if list[x] > max:
            max = list[x]
    print(max)
maximum([37,2,1,-9])

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    min = list[0]
    max = list[0]
    sum = list[0]
    average = list[0]
    length = len(list)
    for x in range(0, len(list)):
        sum = sum + list[x]
        if list[x]<min:
            min = list[x]
        if list[x]>min:
            max = list[x]
    average = sum/length
    print('sumTotal:'+str(sum)+','+"average:"+str(average)+','+'minimum:'+str(min)+','+'maximum:'+str(max)+','+'length:'+str(length))
ultimate_analysis([37,2,1,-9])

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    if len(list) < 2:
        return
    for x in range(0, len(list)):
        temp = list[-1-x]
        if x < len(list) - 1 - x:
            list[-1-x] = list[x]
            list[x] = temp
        else:
            break
    print(list)
reverse_list([37])
reverse_list([37,2,1,-9])
