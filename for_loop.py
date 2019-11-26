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
    i+1
