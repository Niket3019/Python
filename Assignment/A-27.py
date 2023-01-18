# 1. Write a python script to create a ArithmeticError

arithmetic = 5/0
print(arithmetic)


# 2. Write a python script to create a ValueError

valueerror = math.sqrt(-19)
print(valueerror)

# 3. Write a python script to handle the ArithmeticError
try:
  arithmetic = 5/0
  print(arithmetic)
except ArithmeticError:
  print('You have just made an Arithmetic error')

# 4. Write a python script to handle a ValueError
import math
try:
    valueerror = math.sqrt(-19)
except ValueError:
   print("Value error")

# 5. Write a python script to handle multiple Exception in one try
import math
try:
    valueerror = math.sqrt(-19)
except ArithmeticError:
  print('You have just made an Arithmetic error')
except ValueError:
   print("Value error")

# 6. Write a python script to create a calculator with 4 basic operations, and handle a 
# maximum number of exceptions.
try:
   print("add")
   add = int(input("enter a first number:")) + int(input("enter a second number"))
   print("sub")
   sub = int(input("enter a first number:")) - int(input("enter a second number"))
   print("div")
   div = int(input("enter a first number:")) / int(input("enter a second number"))
   print("mul")
   mul = int(input("enter a first number:")) * int(input("enter a second number"))
   print(add)
   print(sub)
   print(div)
   print(mul)
except ArithmeticError:
  print('You have just made an Arithmetic error')
except ValueError:
   print("Value error")
# 7. Write a python script to add a finally block for the above script
try:
  arithmetic = 5/0
  print(arithmetic)
except ArithmeticError:
  print('You have just made an Arithmetic error')
finally:
   print("i don't know")
# 8. Write a python script to implement try except and else block for division

try:
  arithmetic = 5/1
  print(arithmetic)
except ArithmeticError:
  print('You have just made an Arithmetic error')
else:
   print(5/2)
finally:
   print("i don't know")

# 9. Write a python script to raise a ValueError.

valueerror = math.sqrt(-19)
print(valueerror)

# 10. Write a python script to implemented a nested Try Except block
try:
  arithmetic = 5/0
  print(arithmetic)
  try:
      arithmetic = 5/1
      print(arithmetic)
  except ArithmeticError:
      print("it is error of 2 try")
except Exception:
      print("it is handling 1 try block")