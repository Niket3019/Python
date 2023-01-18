# 1. Write a python script to print MySirG N times on the screen
a = "MySirG"
b = int(input("enter a numter to print N time MysirG:"))
while a == 'MySirG':
    a *= b
    print(a)

# 2. Write a python script to print first N natural numbers
a = int(input("minimum natural number enter: "))
b = int(input("maximum natural number enter: "))
while a<=b:
    print(a)
    a += 1

# 3. Write a python script to print first N natural numbers in reverse order
a = int(input("maximum natural number enter: "))
b = int(input("minimum natural number enter: "))
while a >= b :
    print(a)
    a -= 1

# 4. Write a python script to print first N odd natural numbers
a = int(input("enter"))
b = int(input("enter"))
while a <= b:
    print(a) 
    a = a+2

# 5. Write a python script to print first N odd natural numbers in reverse order
a = int(input())
b = 1
while b<a:
    if b%2 != 0:
        print(b)
    b +=1

# 6. Write a python script to print first N even natural numbers
a = int(input("enter"))
b = int(input("enter"))
while a <= b:
    if a%2 == 0:
        print(a)
        a = a+2

#  7. Write a python script to print first N even natural numbers in reverse order
a = int(input('enter'))
while a>=1:
    print(a)
    a = a-1

# 8. Write a python script to print squares of first N natural numbers
a = int(input('enter'))
b = int(input('enter'))
while a <= b:
    c = a**2
    print(c)
    a = a+1

# 9. Write a python script to print cubes of first N natural numbers
a = int(input('enter'))
b = int(input('enter'))
while a <= b:
    c = a**3
    print(c)
    a = a+1
    
# 10. Write a python script to print first 10 multiples of N
a = int(input('enter'))
b = int(input('enter'))
while a<=b:
    c = a*5
    print(c)
    a += 1

   
