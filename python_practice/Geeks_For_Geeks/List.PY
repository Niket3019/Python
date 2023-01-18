# Python program to interchange first and last elements in a list
def swaplist(list):
  list = [12,35,9,56,24]
  size = len(list)
  temp=list[0]
  list[0]=list[size-1]
  list[size-1]=temp
  return list
print(swaplist(list))

# The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].
def swapList(newList):
    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp
    return newList
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped. 
def SwapList(List):
  get = List1[-1],List1[0]
  List1[0],List1[-1] = get
  return List
List1 = [12, 35, 9, 56, 24]
print(SwapList(List1))

# Using * operand. 
# This operand proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name. 
def Swapping(list):
  start,*middle,end = list
  list = [end,*middle,start]
  return list
new = [12, 35, 9, 56, 24]
print(Swapping(new))

# Swap the first and last elements is to use the inbuilt function list.pop(). Pop the first element and store it in a variable. Similarly, pop the last element and store it in another variable. Now insert the two popped element at each other’s original position. 
def Swap(list):
  first = list.pop(0)
  last = list.pop(-1) 
  list.insert(0,last)
  list.append(first)
  return list
list1 = [12, 35, 9, 56, 24]
print(Swap(list1))

#Simple swap, using comma assignment 
#Since the positions of the elements are known, we can simply swap the positions of the elements.
def swapPositions(list, pos1, pos2):    
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [23, 65, 19, 90]
print(swapPositions(List,0,-1))

#  Using Inbuilt list.pop() function 
#Pop the element at pos1 and store it in a variable. Similarly, pop the element at pos2 and store it in another variable. Now insert the two #popped element at each other’s original position.
def Swap(list,pos1,pos2):
  first = list.pop(pos1)
  last = list.pop(pos2)
  list.insert(pos1,last)
  list.insert(pos2,first) 
  return list
pos1,pos2 = 0,-1
List = [1,2,3,4,5]
print(Swap(List,pos1,pos2))
 
#  Demonstrating finding length of a list using the Naive Method
def Length(list1):
     list1 = 0
     list = [9,2,3,4,5]
     for i in list:
      list1 +=1
     return list1
print(Length(list))

# Demonstrating finding length of list using len() and length_hint() 
from operator import length_hint
list = [1,2,34,5]
print(str(list))
len = len(list)
hint = length_hint(list)
print("the len is,"+str(len))
print("the length_hint is,"+str(hint))

# This is the naive approach where we will compare two numbers using if-else statement and will print the output accordingly.
def maximum(a,b):
  if a>b:
    return "a is grater"
  else:
     return "b is greater"
a = int(input("put 1 number"))
b = int(input("put 2 number"))
print(maximum(a,b))

# Count positive and negative numbers from given list using for loop Iterate each element in the list using for loop and check if num >= 0, the condition to check positive numbers. If the condition satisfies, then increase pos_count else increase neg_count. 
list = [1,2,3,-19,-11,4,6,10,-12,-14]
count = 0
count1 = 0
for i in list:
  if i >=0:
    count+=1
    
  else:
     count1+=1
     
print("the negative value in list are :",count1)
print("the positive number in list are :",count)

# Using while loop 
list = [1,2,3,-19,-11,4,6,10,-12,-14]
count = 0
count1 = 0
num = 0
while len(list)>num:
  if list[num]>=0:
    
    count += 1
  else:
    count1+=1
  num+=1
print("the negattive",count1)   
print("the positive",count)

# Reversing a list using the reversed() and reverse() built-in function
lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)
 
print("Using reversed() ", list(reversed(lst)))

# Reversing a list using a two-pointer approach

def revesed(arr):
 left = 0
 right = len(arr)-1
 while left < right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left+=1
    right-=1
 return arr
arr = [1,2,3,4,5,6]
print(revesed(arr))

# Reversing a list using the insert() function
list1 = [1,2,33,4,56,54]
l = []
for i in list1:
     l.insert(0,i)
print(l)

# Reversing a list using list comprehension
original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i] for i in range(1, len(original_list)+1)]
print(new_list)

# Using remove() method
list1 = [1,2,33,[],[],[],234,23,[],[],23432,234,[],32,[],[],[],[],[],[],23,21,123,123,343,123,123,3234]
for i in list1:
    for c in list1:
     if c == []:
        list1.remove(c)
print(list1)

# Using remove() method
list1 = [1,2,33,[],[],[],234,23,[],[],23432,234,[],32,[],[],[],[],[],[],23,21,123,123,343,123,123,3234]
while [] in list1:
    list1.remove([])
print(list1)

# Using enumerate function
list1 = [1,2,33,[],[],[],234,23,[],[],23432,234,[],32,[],[],[],[],[],[],23,21,123,123,343,123,123,3234]
list2 = [ x for i, x in enumerate(list1) if x!=[]]
print(list2)

# 