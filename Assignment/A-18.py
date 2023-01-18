# 1. Write a python program to create and print a dictionary which stores your information.(name, age, gender .....)
info = {'name':input("enter you name"),'age':input("enter you age"),'gender':input("enter your  gender"),'occupation':input('enter your occu')}
print(info)

# 2. Write a python program to access the items of a dictionary by referring to its key name.
a = {1:'niket',2:'saurav',3:'rahul',4:'vineet'}
print(a[1])

# 3. Write a python program to get a list of the values from a dictionary.
a = {1:'niket',2:'saurav',3:'rahul',4:'vineet'}
print(a.values())

# 4. Write a python program to change the value of a specific item by referring to its key name.
a = {1:'niket',2:'saurav',3:'rahul',4:'vineet'}
a[1]='rohit'
print(a)

# 5. Write a python program to print all key names in the dictionary, one by one.
a = {1:'niket',2:'saurav',3:'rahul',4:'vineet'}
for e in a:
    print(e)
# 6. Write a python program to create a dictionary that contains three dictionaries.(nested)
a = {1:{1.1:'niket',1.2:'aditya',1.3:'sujal'},2:{2.1:'vaish',2.2:'varun',2.3:'suraj'}}
print(a)

# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
a = {1:'niket',2:'varun'}
b = {3:'niket',4:'saurav',5:'rahul',6:'vineet'}
c = {7:'niket',8:'saurav',9:'rahul',10:'vineet'}
niket = {}
for e in a,b,c: 
 niket.update(e)
print(niket)

# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e','f','g','h','i','j']

dict = {}
dict = {list1[e]:list2[e] for e in range(len(list2))}
print(dict)

# 9. Write a python program to merge two python dictionaries into one dictionary.
a = {1:'niket',2:'varun'}
b = {3:'niket',4:'saurav',5:'rahul',6:'vineet'}
niket = {}
for e in a,b: 
 niket.update(e)
print(niket)
# 10. Write a python program to get the key of lowest value from the dictionary.sample_dict = {'C': 92,'Java': 66,'Python': 85}
sample_dict = {'C': 92,'Java': 66,'Python': 85}
a = sorted(sample_dict)
for e in a:
    print(e)
    break