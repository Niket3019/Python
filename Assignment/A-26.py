# 1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.
from threading import Thread


class overloading:
    def add(self,a1,a2):
        print(a1+a2)
    def add(selff,a1,a2,a3):
        print(a1+a2+a3)
adding = overloading()

adding.add(1,2,3)

# 2. Write a python script to create a user account class with 2 instance variables (userid and balance). 
# Create 3 user objects and add all the users using operator overloading.
class user_account:
   def __init__(self,userid,balance):
         self.userid=userid
         self.balance=balance
   def __add__(self,other):
     total1 = self.userid + other.userid
     total2 = self.balance + other.balance
     Total_all = user_account(total1,total2)
     return Total_all
   def __str__(self):
       return self.userid + ":" + str(self.balance)
a1 = user_account("Niket",1000)
a2 = user_account("Rahul",1000)
Total_all = a1 + a2
print(Total_all)
# 3. Write a python script to create a to print the above user account object using operator overloading (hint __str__ method).
class user_account:
   def __init__(self,userid,balance):
         self.userid=userid
         self.balance=balance
   def __add__(self,other):
     total1 = self.userid + other.userid
     total2 = self.balance + other.balance
     Total_all = user_account(total1,total2)
     return Total_all
   def __str__(self):
       return self.userid + ":" + str(self.balance)
a1 = user_account("Niket",1000)
a2 = user_account("Rahul",1000)
Total_all = a1 + a2
print(Total_all)
# 4. Write a python script to create two Threads. First thread will print all Even numbers and Second thread 
# will print all Odd numbers till 100.
from threading import *
from time import sleep
class Even(Thread):
   def even(self):
     for i in range(1,100+1):
      if i%2==0:
       print(i)
       sleep(1)
class Odd(Thread):
  def odd(self):
    for i in range(1,100+1):
      if i%2!=0:
        print(i)
        sleep(1)
even  = Even()
odd = Odd()
even.even()

odd.odd()
# 5. Write a python script to create 2 threads to add all the values from 1 to 100.
from threading import *
from time import sleep
class Add1(Thread):
   def add(self):
     c = 0
     for i in range(1,100):
       c+=i
       print(c)
       sleep(1)
class Add2(Thread):
   def add2(self):
     c = 0
     for i in range(50,100):
       c+=i
       print(c)
       sleep(1)
add50  = Add1()
add100 = Add2()
add50.add()
add100.add2()
# 6. Write a python script to create 5 threads to fill a list with random numbers till 100.
from threading import *
from time import sleep
import random
random_list = []
class Random1(Thread):
   def random1(self):
    
    n = random.randint(0,25)
    random_list.append(n)
    print(random_list)
    sleep(1)
class Random2(Thread):
   def random2(self):
 
    n = random.randint(25,50)
    random_list.append(n)
    print(random_list)
    sleep(1)
class Random3(Thread):
   def random3(self):
   
    n = random.randint(50,75)
    random_list.append(n)
    print(random_list)
    sleep(1)
class Random4(Thread):
   def random4(self):
    
    n = random.randint(75,90)
    random_list.append(n)
    print(random_list)
    sleep(1)
class Random5(Thread):
   def random5(self):

    n = random.randint(90,100)
    random_list.append(n)
    print(random_list)
    sleep(1)
   
random1to25 = Random1()
random25to50 = Random2()
random50to75 = Random3()
random75to90 = Random4()
random90to100 = Random5()
random1to25.random1()
random25to50.random2()
random50to75.random3()
random75to90.random4()
random90to100.random5()
# 7. Write a python script to create a clock where 1st thread will print the current time every second and 2nd
#  will print “1 Minute Completed” after every 1 minute.
from threading import *
from time import sleep
import datetime
class Minute1(Thread):
   def add(self):
      for i in range(0,61):
        i+=0
        now = datetime.datetime.now()
        print("current date and time :",now.strftime("%d-%m-%y  %H:%M:%S %p"))
        sleep(1)
class Minute2(Thread):
   def add2(self):
     print("one minutes completed!")
     
add_min1  = Minute1()
add_min2 = Minute2()
add_min1.add()
add_min2.add2()
# 8. Write a python script to change the name of the Thread.
from concurrent.futures import thread
from threading import*
import threading
class change_name(threading.Thread):
   def __init__(self,name):
      threading.Thread.__init__(self)
      self.name = name
   def show(self):
      print(self.name)
thread1 = change_name("niket")
thread1.name = "rahul"
thread1.show()
# 9. Write a python script to join 2 threads after printing completing the first Question.
# 10. Write a python script to check whether a given number is prime or armstrong number
# using 2 different threads.