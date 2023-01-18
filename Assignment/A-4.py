# 1. Write a python script to take your name as input from the user and then print it.
a = input("enter your name")
print(a)

# 2. Write a python script to take input from the user. Input must be a number.
b =  input(23)
print(b)

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
ab = int(input("Enter the first value:"))
bc = int(input("Enter the second value:"))
c = ab + bc
print(c)

# 4. Write a python script which takes the radius from the user and display area of a circle.
radius = int(input("Enter the radius of the circle:"))
areaofcircle = 3.14 * radius**2
print(areaofcircle)

# 5. Write a python script to calculate the square of a number. Number is entered by the user.
number = int(input("Enter the square of number:"))
number *= number
print(number)

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
base = int(input("Enter the base value:"))
height = int(input("Enter the height value"))
areaoftriangle = (base * height)/2
print("the area of triangle is :",areaoftriangle)

# 7. Write a python script to calculate average of three numbers, entered by the user
num1 = int(input("Enter First Value:"))
num2 = int(input("Enter second value:"))
num3 = int(input("Enter the three value"))
average = (num1+num2+num3)/3
print("The Average value is:",average)

# 8. Write a python script to calculate simple interest
principle = int(input("Enter the principle value:"))
time = int(input("Enter the time value:"))
rate = int(input("Enter the rate value:"))
simpleinterest = (principle*time*rate)/100
print("the simple S.I vale is:",simpleinterest)

# 9. Write a python script to calculate the volume of a cuboid.
length = int(input("Enter the length value:"))
width = int(input("Enter the width value:"))
height = int(input("Enter the height value:"))
volumeofcuboid = length*width*height
print("the value of VOC is:",volumeofcuboid)

# 10. Write a python script to calculate area of a rectangle
length1 = int(input("Enter the length value:"))
width1 = int(input("Enter the width value:"))
rectangle = length1*width1
print("the value of rectangle is:",rectangle)