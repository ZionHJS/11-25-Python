# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print('Hello', name)  # with a comma
print('Hello' + name)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print('Hello', name')  # with a comma
print('Hello' + name)  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print(f'I love eat {fave_food1} and {fave_food2}.')  # with an f string
print('I love to eat {} and {}'.format(
    fave_food1, fave_food2))  # with .format()


first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


# code block
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

# pass


class EmptyClass:
    pass


for val in my_string:
    pass

# data-types
# Primitive data types
# Boolean Values
is_hungry = True
has_freckles = False
# Numbers
age = 35
weight = 160.57
# Strings
name = 'Joe Blue'

# Composite types
# Tuples -A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
# immutable
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
# ERROR: cannot be modified ('tuple' object does not support item assignment)
dog[1] = 'dachshund'

# Lists -A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
# kind of like Array in javascript???
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)  # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)  # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)  # output: ['Francis', 'Oliver']

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods here.
# kind of like JSON???
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'  # updates if the key exists
# adds a key-value pair if the key doesn't exist
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')  # removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

# find out data-type
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# find out data-length
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))  # output: 11

# Type Casting or Explicit Type Conversation
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# Conditional Statement
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute
x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false

if not True == False:  # true
    print('true')
if !True == False:  # SyntaxError
    print('true')

# loops
for x in range(0, 10, 1):
for x in range(0, 10):  # increment of +1 is implied
for x in range(10):  # increment of +1 and start at 0 is implied

    # Note that if you need to specify increment other than +1, all three arguments are required
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# for loop through dictionaries
my_dict = {"name": "Noelle", "language": "Python"}
for k in my_dict:
    print(k)
# output: name, language

# all for dictionaries
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# to iterate through the values
for val in capitals.values():
    print(val)
# to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)

# While Loops
for count in range(0, 5):
    print("looping - ", count)
# while loop
count = 0
while count < 5:
    print("looping - ", count)
    count += 1
# while else
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# break
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r
# continue
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
