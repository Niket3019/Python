# 1. Write a python script to add comments and print “Learning Python” on screen.
# Hello this tag is comment
a = "Learning python"
print(a)

# 2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.
""" Above tag is use to add multiple comment on screen"""
a = 45
b = 7327
c = 3984732
d = "Niket"
print(a)
print(b)
print(c)
print(d)

# 3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
ab = 37643
print(type(ab))

bc = True
print(type(bc))

cd = "Niket"
print(type(cd))

ad = 3+4j
print(type(ad))

# 4. Write a python script to print the id of two variables containing the same integer values.
a = 54
b = 54
print(a, b)

# 5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
abc = 270
print(type(abc), id(abc))
name = "Raj"
print(type(name), id(name))
value = 3+75467j
print(type(value), id(value))
xyz = False
print(type(xyz), id(xyz))

# 6. Write a python script to print all the keywords
import keyword
from re import M
print(keyword.kwlist)

# 7. On Python shell use help() function and display the list of keywords
help('keywords')

# 8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py
import A0

# 9. Name the keywords, used as data in the Python script.
#control flow keyword : else,elif,if

#10.import datetime
import datetime
now = datetime.datetime.now()
print("current date and time :",now.strftime("%d-%m-%y  %H:%M %p"))


