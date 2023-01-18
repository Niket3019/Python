# 1. Write a python script to check whether a given number is positive or non-positive
a = int(input("Enter the number: "))
if a>0 :
    print("positive")
else :
    print("non-positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not
a = int(input("Enter the number: "))
if a%5 == 0 :
    print("it is divisible")
else :
    print("it is not divisible")

# 3. Write a python script to check whether a given number is even or odd
a = int(input("Enter the number: "))
if a%2 == 0 :
    print("it is even")
else :
    print("it is odd")

# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num1 > num2 :
    print("Num1 is greater the Num2")
elif num1 == num2 :
    print("both num are same")
else :
    print("Num2 is greater than Num1: ")

# 5. Write a python script to print two given words in dictionary order
print("Enter Two Cities")
a,b = input(),input()
if a>b :
    print(b,a) 
else :
    print(a,b)

# 6. Write a python script to check whether a given number is a three digit number or not.
a = int(input("Enter the number: "))
if a>=100 and a<=999 :
    print("Number are three digit: ")
else :
    print("number are not three digit")

# 7. Write a python script to check whether a given number is positive, negative or zero
a = int(input("Enter any number: "))
if a > 0 :
    print("it is positive")
elif a < 0 :
    print("it is negative")
else :
    print("it is zero")

# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
from math import sqrt
print("Enter the quadratic equation: ")
a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c

if D>0 :
    x1 = (((-b) - sqrt(D))/(2*a))
    x2 = (((-b) + sqrt(D))/(2*a))
    print("The two real & distinct roots: ",x1,x2)
elif D == 0 :
    x = (-b) / 2*a
    print("it is real & equal root", x)
else :
    print("It is imaginary:")

# 9. Write a python script to check whether a given year is a leap year or not.
print("enter the year: ")
year = int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("it is leap year")
else :
    print("it is not a leap year")

# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
print("enter the number: ")
number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1>number2>number3 :
    print("number1 is greater")
elif number2>number1>number3 :
    print("number2 is greater")
elif number3>number1>number2 :
    print("number3 is greater")
else :
    print("all number are same ")

# 11. Write a python script to take the month value in numeric format and display the number of days in it.
MonthNumber = int(input("enter the month number: "))
if MonthNumber == (1,3,5,7,8,10,12) :
    print("31 days")
elif MonthNumber == (2) :
    print("28/27 days")
else :
    print("30 days")

# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
real = int(input("enter the number"))
imaginary = int(input("enter the number"))
z = complex(real,imaginary)
if real>imaginary :
    print("real is greater")
else :
    print("imaginary is greater")



