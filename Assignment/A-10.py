# 1. Write a python script to print MySirG N times on the screen
a = 'MySirG'
for e in a :
  print(a)

# 2. Write a python script to print first N natural numbers
a = int(input("any rang of natural number"))
for e in range(0, int(a)) :
   print(e, end = ' ')

# 3. Write a python script to print first N natural numbers in reverse order
a = int(input("any rang of natural number"))
for e in range(a,0,-1) :
   print(e, end = ' ')

# 4. Write a python script to print first N odd natural numbers
a = int(input("enter number:"))
for e in range(1,a,2):
    print(e)

# 5. Write a python script to print first N odd natural numbers in reverse order
a = int(input("enter number:"))
for e in range(a-1,0,-2):
    print(e)

# 6. Write a python script to print first N even natural numbers
a = int(input("enter number:"))
for e in range(0,a,2):
    print(e)

# 7. Write a python script to print first N even natural numbers in reverse order
a = int(input("enter number:"))
for e in range(a,0,-2):
    print(e)

# 8. Write a python script to print squares of first N natural numbers
a = int(input("enter number:"))
for e in range(0,a):
    print(e**2)

# 9. Write a python script to print cubes of first N natural numbers
a = int(input("enter number:"))
for e in range(0,a):
    print(e**3)
    
# 10. Write a python script to print first 10 multiples of Nq
a = int(input("enter a number"))
for e in range(0,11):
    print(e*a)