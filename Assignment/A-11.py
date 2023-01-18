# 1. Write a python script to calculate sum of first N natural numbers
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)

# 2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1+=n*n
    n=n-1 
print("The sum of squares of first N natural numbers",sum1)

# 3. Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1+=n*n*n
    n=n-1
print("The sum of first n natural numbers is",sum1)

# 4. Write a python script to calculate sum of first N odd natural numbers
num = int(input("Print sum of odd numbers till : "))
sum = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        sum += i

print("\nSum of odd numbers from 1 to", num, "is :", sum)

# 5. Write a python script to calculate sum of first N even natural numbers
num = int(input("Print sum of odd numbers till : "))
sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        sum += i

print("sum of first N even natural numbers", num, "is :", sum)

# 6. Write a python script to calculate factorial of a given number
num = int(input("factorial number : "))
sum = 1

for i in range(1, num + 1):
        sum *= i

print("factorial of a given number", num, "is :", sum)

# 7. Write a python script to count digits in a given number
num = int(input("Enter a numer \n"))
count = 0
while num>0:
    count +=1
    num = num//10
    
print("count digits in a given number",count)

#8. Write a python script to calculate sum of digits of a given number
a = int(input("enter a number:" ))
total = 0
while (a>0):
   tot = a%10
   total = total + tot
   a = a//10
print("the sum of number",total)

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
n=int(input("Enter a number: "))
a = []
while(n>0):
    tot=n%2
    a.append(tot)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
print(a)

# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
n=int(input("Enter a number: "))
a = []
while(n>0):
    tot=n%8
    a.append(tot)
    n=n//8
a.reverse()
print("octal equivalent is: ")
print(a)
 


    