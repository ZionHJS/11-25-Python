<result_if_true> if <condition> else<result_if_false>

#Lambdas
def square(num):
    x = num ** 2
    return x
    
#turn it into anonymous(lambda) function
lambda num: num ** 2   #This means "here is an anonymous (nameless) function that takes one argument, called num, and returns num**2.

#a anonymous function that takes two arguments and returns the sum of the two arguments
lambda num1, num2: num1 + num2

#define a function and unnecessarily consume memory and complicate our code, just to produce the same result:
my_arr = [1,2,3,4,5]
print(list(map(lambda x: x**2, my_arr)))

