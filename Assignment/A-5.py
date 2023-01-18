# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
a = 2534//10
print(a)

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
a = 2089%10
print(a)

# 3. Write a python script to swap data of two variables
a = 23
b = 12
a,b = b,a
print(a)
print(b)

# 4. Write a python script to find x power y, where values of x and y are given by user
x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
z = x**y
print(z)

# 5. Write a python script which takes a three digit number from the user and displays only its first digit.
first = int(input("enter the first digit number:"))
second = int(input("enter the second digit number:"))
third = int(input("enter the third digit number:"))
print(first)

# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.
first = int(input("enter the first digit number:"))
second = int(input("enter the second digit number:"))
third = int(input("enter the third digit number:"))
print(second)

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.
first = int(input("enter the first digit number:"))
second = int(input("enter the second digit number:"))
third = int(input("enter the third digit number:"))
print(third)

# 8. Write a python script to use IN operator to display the data present in the list
x = "niket,singh"
print("ni" in x)

# 9. Write a python script to use NOT IN operator to display the data not present in list
x = "sauva pandey"
print("sau" not in x)

# 10. Write a python script to use IS operator to display if both variables are the same object or not?
xyz = 438876437
abc = 438876437
print(xyz is abc)
print(xyz is not abc)

