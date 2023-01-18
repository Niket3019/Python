# 1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
a = ["java","python","sql","c"]
print(a)

# 2. Write a python script to get the data type of a list.
a = ["java","python","sql","c"]
print(type(a))

# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["java","c","python"]
print(mylist[-1])

# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

thislist[1]="NoSql"
thislist[3]="flutter"
print(thislist)

#5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("python")
print(mylist)

# 6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"] 
secondlist = ["C", "Cpp", "NoSQL"]
firstlist.append(secondlist)
print(firstlist)

# 7. Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java","SQL", "C", "Reactnative", "Javascript", "Python"]
for a in thislist:
 print(a)
# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

# 9. Write a Python script to create a list of city names taken from the user.
city = []
city=[cities for cities in input().split()]
print(city)

# 10. Write a Python script to create a list, where each element of the list is a digit of a given number.
num_list = []
number = int(input("enter a number of how many number you want to put"))
for i in range(0, number):
    element = int(input())
    num_list.append(element)
    print(num_list)