import random
x = [[5,2,3],[10,8,9]]
students = [
    {'first_name':'Michael', 'last_name':'jordan'},
    {'first_name':'John', 'last_name':'Rosales'}
]
sports_directory = {
    'basketball':['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer':['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x':10, 'y':20}]

#1.Change the value 10 in x to 15, once you're done, x should now be [[5,2,3],[15,8,9]
x[1][0] = 15
print(x)   #15

#2.Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0])

#3.In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#4.Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#@2-Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def key_and_value(list):
    for i in list:
        print(i)
key_and_value(students)

#@3-Get Values From a List of Dicrtionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key, list):
    for i in list:
        print(i[key])
iterateDictionary2('first_name', students)

#4. iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dic):
    print((len(dic['locations'])), "LOCATIONS",(dic['locations']))
    print((len(dic['instructors'])), 'INSTRUCTORS', (dic['instructors']))
printInfo(dojo)