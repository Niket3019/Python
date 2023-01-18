# 1. Use iter and next method to access all the elements of a given set using while loop
a={1,2,3,4,5}
b = iter(a)
while True:
   try:
    print(b.__next__())

   except:
      break

# 2. Create a generator to produce first n odd natural numbers
def odd(n):
 a=1
 while n:
    yield a
    a+=2
    n-=1
for e in odd(10):
    print(e,end=' ')

# 3. Create a generator to produce first n even natural numbers
def odd(n):
 a=1
 while n:
    yield a
    a+=1
    n-=1
for e in odd(10):
    print(e,end=' ')

# 4. Create a generator to produce squares of first N natural numbers
def sqare(n):
 a=1
 while n:
    yield a*a
    a+=1
    n-=1
for e in sqare(10):
    print(e,end=' ')

# 5. Create a generator to produce first n terms of Fibonacci series
def odd(n):
 a,b=0,1
 while n:
    yield a
    a,b=b,a+b
    n-=1
for e in odd(10):
    print(e,end=' ')

# 6. Create a generator to produce first n prime numbers
def isprime(num):
   for i in range(2,num):
      if num%i==0:
         return False
   return True
def primegenerator(n):
   num=2
   while n:
      if isprime(num):
         yield num
      n-=1
      num+=1
   return
it = primegenerator(10)
for e in it:
   print(e,end=' ')
   
# 7. Create an endless iterator using generator method to produce terms of Fibonacci series