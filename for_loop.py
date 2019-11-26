# print all integers from 0 to 150
i = 0
while i <= 150:
    print(i)
    i = i+1

# print all the multiples of 5 from 5 to 1,000
i = 0
while i <= 1000:
    print(i)
    i = i + 5

# print integers 1 to 100 if divisible by 5, pirnt "Coding" instead. if divisible by 10, print "Coding Dojo"
i = 1
while i <= 100:
    if i%10 == 0:
        print('Coding Dojo')
    elif i%5 == 0:
        print('Coding')
    else:
        print(i)
    i = i+1

# add odd integers from 0 to 500,000 and print the final sum
i = 1
sum = 0
while i < 500000:
    if i > 500000-2:
        print(sum)
    sum = sum + i
    i = i + 2

# print positive numbers starting at 2018, counting donw by fours
i = 2018
while i > 0:
    print(i)
    i = i - 4

# set three variables:lowNum, highNum, mult, starting at lowNum and going through highNum, print only the integers that are a multiple of mult
lowNum = 3
highNum = 30
mult = 3
x = 0
for x in range(lowNum, highNum + 1, mult):
    print(x)