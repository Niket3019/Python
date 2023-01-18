# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
def uniquelist(b):
  x = []
  for a in b:
    if a not in x:
      x.append(a)
  print(x)

uniquelist([12,22,33,33,3,3,42,5])

# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
"""3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(num):
   for i in num:
    if i%2==0:
     print(i)
even(List1)
# 5. Write a python program to create a function to find the Min of three numbers.
def num(s):

     print(min(s))
tuple1 = (12,43,11)
num(tuple1)
# 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def num(a,b):
    list1 = []
    for i in range(a,b+1):
        list1.append(i*i)
    print(list1)
num(1,30)

# 7. Write a python program to access a function inside a function.
def fun(a):
    def fun1(b):
        print(b)
    fun1(34)
    print(a)
fun(3)

# 8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
str1 = "NiketSingh"
string_test(str1)
# 9. Write a python program to create a function to check whether a string is a pangram or not.