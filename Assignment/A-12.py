# 1. Write a python script to reverse a number.
a = int(input("enter a number to reverse"))
num = 0
while a>0:
     n = a%10
     num = num*10 + n
     a = a//10
print(str(num))

# 2. Write a python script to check whether a given number is Prime or not
num = int(input("enter a number"))
for i in range(2,int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
else:
        print(num, "is a prime number")

# 3. Write a python script to print all Prime numbers under 100
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        
        if(Number % i == 0):
            count = count + 1
     
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
a = int(input())
b = int(input())
for Number in range (a, b):
    count = 0
    for i in range(2, (Number//2 + 1)):
        
        if(Number % i == 0):
            count = count + 1
     
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
# 5. Write a python script to find next prime number of a given number