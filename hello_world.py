# 1. TASK: print "Hello World"
print( 'Hello World' )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( 'Hello', name )	# with a comma
print( 'Hello' + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( 'Hello', name' )	# with a comma
print( 'Hello' + name )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( f'I love eat {fave_food1} and {fave_food2}.') # with an f string
print( 'I love to eat {} and {}'.format(fave_food1, fave_food2)) # with .format()

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#code block
x = 10
if x > 50:
	print("bigger than 50")
else:
	print("smaller than 50")
