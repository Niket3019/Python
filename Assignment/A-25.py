# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).
class Profile:
    def __init__(self,name,email,age):
            self.name = name
            self.email = email
            self.age = age
    def show(self):
        print(self.name,self.email,self.age)
obj1 = Profile("Niket","niketsingh199@gmail.com","20")
obj1.show()
# 2. Write a python script to update the above Profile class with encapsulation.
class Profile:
    def __init__(self,name,email,age):
            self.name = name
            self.email = email
            self.age = age
    def show(self):
        print(self.name,self.email,self.age)
    def set(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
obj1 = Profile("Niket","niketsingh199@gmail.com","20")
obj1.set("Rahul","rahul199@gmail.com",20)
obj1.show()
# 3. Write a python script to update 2nd Question, change email and age to __email and __age.
class Profile:
    def __init__(self,name,email,age):
            self.name = name
            self.__email = email
            self.__age = age
    def show(self):
        print(self.name,self.__email,self.__age)
    def set(self,name,email,age):
        self.name = name
        self.__email = email
        self.__age = age
obj1 = Profile("Niket","niketsingh199@gmail.com","20")
obj1.set("Rahul","Niket199",20)
obj1.show()
# 4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.
class Profile:
    Name = "platform"
    @classmethod
    def classmethod(self):
      print(self.Name)
    def __init__(self,name,email,age):
            self.name = name
            self.email = email
            self.age = age
    def show(self):
        print(self.name,self.email,self.age)
    def set(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
obj1 = Profile("Niket","niketsingh199@gmail.com","20")
obj1.set("Rahul","rahul199@gmail.com",20)
obj1.show()
Profile.classmethod()
# 5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
class AddSub:

    def AddSub(x,y):
        print(x+y,x-y)       

add = AddSub()
AddSub.AddSub(10,12)
# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it 
# from the Calculator class.
class Calculator:
    @staticmethod
    def mul(x,y):
        print(x*y)
    @staticmethod
    def div(x,y):
        print(int(x/y))
class Calculator2(Calculator):
    print("i am inherit")
a = Calculator2()
a.mul(12,10)
a.div(12,2)
# 7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).
class Phone:
    @staticmethod
    def calling():
        print("calling:""Anonymous Call Rejection \nPriority Ringing")
    @staticmethod
    def sms():
        print("sms:""It's automatic \nIt can be expanded")
a = Phone()
a.sms()
a.calling()
# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.
class Calculator:
    @staticmethod
    def mul(x,y):
        print(x*y)
    @staticmethod
    def div(x,y):
        print(int(x/y))
class Calculator2(Calculator):
    print("i am inherit")
a = Calculator2()
a.mul(12,10)
a.div(12,2)
class Phone:
    @staticmethod
    def calling():
        print("calling:""Anonymous Call Rejection \nPriority Ringing")
    @staticmethod
    def sms():
        print("sms:""It's automatic \nIt can be expanded")
a = Phone()
a.sms()
a.calling()
class SmartPhone(Calculator2,Phone,Calculator):
    pass
abc = SmartPhone()
# 9. Write a python script to create an application like Truecaller where names and numbers are stored. Truecaller class
#  will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).

# 10. Write a python script to add the new method in SmartPhone class which accepts
#Truecaller object as a parameter and call the fetch method of Truecaller.