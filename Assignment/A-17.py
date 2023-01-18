# 1. Write a python program to store all the programming languages known to you using Set.
s = {"c","c++","java","javascript","python","c#","R","go"}
print(s)

# 2. Write a python program to store your own information {name, age, gender, so on..}
s = {"name:niket","age:20","gender:male","occupation:tyit"}
print(s)

# 3. Write a python script to get the data type of a Set.
s = {"niket","rahul","saurav"}
print(type(s))

# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}
thisset = {"Java", "Python", "Django"}
if "Python" in thisset:
 print("true")
else:
 print("false")

# 5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"}
thisset = {"Java", "Python", "SQL"}
newset = {"Djago","Springboot","MongoDB"}
thisset.update(newset)
print(thisset)

# 6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print(thisset)

# 7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset = {"Python", "Django", "JavaScript","SQL"}
thisset.remove('SQL')
print(thisset)

# 8. Write a python program to delete the set completely.
isset = {"Python", "Django", "JavaScript","SQL"}
isset.clear()

# 9. Write a python program to loop through the set and print values thisset = {"Python", "Django", "JavaScript", “SQL”}
isset =  {"Python", "Django", "JavaScript", "SQL"}
for a in isset:
    print(a)
    
# 10. Write a python program to find the maximum and minimum value in a set.
isset =  {"Python", "Django", "JavaScript", "SQL"}
print("the max value is:",max(isset),"the min value is:",min(isset))