# 1. Write a recursive python function to print first N natural numbers.
def natural(n):
    if n>0:
     natural(n-1)
     print(n)
natural(10)
# 2. Write a recursive python function to print first N natural numbers in reverse order
def natural(n):
    if n>0:
     print(n)
     natural(n-1)
     
natural(10)
# 3. Write a recursive python function to print first N odd natural numbers
def natural(n):
    if n==1:
        print(1)
    else:
     natural(n-1)  
     print((2*n)-1)     
natural(5)

# 4. Write a recursive python function to print first N odd natural numbers in reverse order
def natural(n):
    if n==1:
        print(1)
    else:
     print((2*n)-1)
     natural(n-1)       
natural(5)
#5. Write a recursive python function to print first N even natural numbers.
def natural(n):
    if n>1:
     natural(n-1)
     print((2*n)-2)
natural(10)
# 6. Write a recursive python function to print first N even natural numbers in reverse order.
def natural(n):
    if n>1:
     print((2*n)-2)
     natural(n-1)
natural(10)

# 7. Write a recursive python function to print squares of first N natural numbers
def natural(n):
    if n>0:
     natural(n-1)
     print(n**2)
natural(10)

# 8. Write a recursive python function to print cubes of first N natural numbers
def natural(n):
    if n>0:
     natural(n-1)
     print(n**3)
natural(10)

# 9. Write a recursive python function to print first N multiples of a given number.
def natural(n):
    if n>0:
     natural(n-1)
     print(n*a)
a = 4
natural(10)

# 10. Write a recursive python function to print a number in reverse order.
def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n//10, r*10 + n%10)
number = int(input("Enter number: "))
reversed_number = reverse(number,0)
print(reversed_number)