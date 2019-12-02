# import the librarycopy
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

defcopy add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y

#import A package
from my_package.subdirectory import my_functions

#Packages are namespaces which contain multiple packages and module themselves. they are simply directories, but with a twist
sample_project
     |_____ python_file.py
     |_____ my_modules
               |_____ __init__.py
               |_____ test_module.py
               |_____ another_module.py
               |_____ third_module.py

import my_modules.test_module 
#or
from my_modules import test_module

