# 1. Write a python program to create a simple function which prints “MySirG” .
def prt():
    a = "mysirg"
    print(a)
prt()
# 2. Write a python program to create a function which expects two arguments and print them in the function body.
def args(a,b):
    c = a+b
    print(c)
args(23,25)
# 3. Write a python program to create a function which expects an unknown number of arguments.
def unknown(a):
    c = a + 10
    print(c)
unknown(int(input("enter a any number:")))
# 4. Write a python program to create a function which expects kwargs arguments.
def kwr(a,b):
    c = a+b
    print(c)
kwr(b=10,a=13)
# 5. Write a python program to create a function which expects a list as an argument.
def listargs(args):

      print(args) 
listargs(["niket","saurav","rahul"])
# 6. Write a python program to create a function that finds a maximum of four numbers.
def maximum(*numbers):
    max_num = max(numbers)
    print(max_num)
maximum(112,222,192,114)
# 7. Write a python program to sum all the numbers in a list.
def maximum(numbers):
    max_num = sum(numbers)
    print(max_num)
maximum([112,222,192,114])
# 8. Write a python program to multiply all the numbers in a list.
def mul(list):
    result = 1
    for e in list:
        result = result*e
    print(result)
list1 = [12,23,182,13]
mul(list1)
# 9. Write a python program to create a function to check whether a number falls in a given range.
def number(tuple1):
   for e in range(50):
     if e in tuple1:
      print("present in range",e)
     else:
         print("not present in range",e)
tuple1 = 12,121,57,22,11,9,50,70,46 
number(tuple1)
  

# 10. Write a python program to create a function to check whether a given number is even or odd.
def mul(list):
    for e in list:
     if e%2==0:
        print("it is even:",e)
     else :
        print("it is odd:",e)
list1 = [12,23,182,13]
mul(list1)