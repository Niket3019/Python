# 1. Write a recursive python function to calculate sum of first N natural numbers
def sum(n):
 if n==0:
    return 1
 return n + sum(n-1)
f = sum(10)
print(f)
# 2. Write a recursive python function to calculate sum of first N odd natural numbers
def odd(n):
 if n==1:
        return 1
 else:
        return (2*n)-1 + odd(n-1)       
a = odd(3)
print(a)
# 3. Write a recursive python function to calculate sum of first N even natural numbers
def even(n):
    if n==1:
        return 0
    else:
        return 2*n-2 + even(n-1)
a = even(6)
print(a)
# 4. Write a recursive python function to calculate sum of squares of first N natural numbers
def square(n):
 if n == 1:
    return 1
 else:
     return n**2 + square(n-1)
b = square(5)
print(b)
# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers
def square(n):
 if n == 1:
    return 1
 else:
     return n**3 + square(n-1)
b = square(5)
print(b)

# 6. Write a recursive python function to calculate the factorial of a number.
def fac(n):
 if n==1 or n==0:
    return 1
 else:
    return n * fac(n-1)
print(fac(5))
# 7. Write a recursive python function to calculate sum of the digits of a given number
def fac(n):
 if n==0:
    return 0
 return n%10 + fac(int(n/10))
print(fac(115))
# 8. Write a recursive python function to print binary of a given decimal number.
def fac(n):
 if n==0:
    return 0
 return n%2+10 * fac(n//2)
print(fac(5))
# 9. Write a recursive python function to print octal of a given decimal number
def fac(n):
 if n==0:
    return 0
 return n%8+10 * fac(n//8)
print(fac(23))
# 10. Write a recursive python function to find the Nth term of the Fibonacci series.
