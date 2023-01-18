#1. Write a Python script to create a list of first N natural numbers.
a = []
number = int(input("enter a max natural number you want put"))
for i in range(1, number):
    a.append(i)
    print("the natural number are in list:",a)

# 2. Write a Python script to create a list of first N odd natural numbers.
a = []
number = int(input("enter a number you want to put a odd one: "))
for i in range(1,number,2):
    a.append(i)
    print("the odd number are:",a)

# 3. Write a Python script to create a list of first N even natural numbers.
a = []
number = int(input("enter a number how much you want to put"))
for i in range(2,number,2):
    a.append(i)
    print(a)

# 4. Write a Python script to find the greatest number in a given list of numbers.
a = [1,3,3,2114,4,32,2]
print(max(a))

# 5. Write a Python script to find the smallest number in a given list of numbers.
a = [12,4245,522,12,234,454,1,4454,1123]
print(min(a))

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
a = [3342,3446,6523,4756,3261,2100,93872]
print(sum(a))

# 7. Write a Python script to remove all non int values from a list.
a = ["niket","saurav",23,"325",True,1256,34.22]
non_int=[x for x in a if not isinstance(x, int)]
print(non_int)

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
a = [1,2,31,32,1,10,1,1,23,31,2,10,10]
distinct = []
distinct = set(a)

print("the unique value is",distinct)
print("the frequency of list are",len(distinct))

# 9. Write a Python script to print indices of all occurrences of a given element in a given list.
thislist = ["Java","SQL", "C", "Reactnative", "Javascript", "Python"]
for a in range(len(thislist)):
 print(a)

# 10. Write a python script to sort a list.
list = ["niket","rahul","zeb","zeb"]
list.sort()
print(list)