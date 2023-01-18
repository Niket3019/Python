# 1. Write a python program to create a user class with 3 properties : name, age, email.
class Computers:
  pass
name = Computers()
name = "Niket"
print(name,type(name))
age = Computers()
age = "20"
print(age)
email = Computers()
email = "Niketsingh199"
print(email)
# 2. Write a python program to create a user class with a method to greet the user.
class greet():
  def __init__(users):
    users.wish = "Have a Great Day"
user = greet()
print(user.wish)
# 3. Write a python program to create 2 objects of the user class and assign different values.
class TvProduct():
    pass
user1 = TvProduct()
user1 = "Samsung"
print(user1)
user2 = TvProduct()
user2 = "MI"
print(user2)
# 4. Write a python program to init default values for user object using __init__ method.
class Bike():
    def __init__(self):
       self.bike = "BMW"
client = Bike()
print(client.bike)
# 5. Write a python program to delete the age property of the user.
# 6. Write a python program to create 3 user objects and find the youngest of all.
class young():
    def __init__(self):
       self.user1 = 20
       self.user2 = 2
       self.user3 = 24
    def show(selfs):
        if selfs.user1>selfs.user2 and selfs.user1>selfs.user3:
            print("user1 is greater")
        elif selfs.user2>selfs.user1 and selfs.user2>selfs.user3:
            print("user2 is greater")
        else:
            print("user3")
user1 = young()
user2 = young()
user3 = young()
young.show(user1)
# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,hdd) and 2 methods (showConfig() to print the values, __init__() 
# to initialize thevalues).
class Laptop():
    def __init__(self,brand,cpu,ram):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
    def show(selfs):
        print(selfs.brand,selfs.cpu,selfs.ram)
com1 = Laptop("Hp","i7","8gb")
com2 = Laptop("Lenovo","i5","32gb")
com3 = Laptop("Dell","i9","16gm")
com1.show()
com2.show()
com3.show()
# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.

class Laptop():
    def __init__(self,brand,cpu,ram):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
    def __repr__(selfs):
        return str((selfs.brand,selfs.cpu,selfs.ram))
com1 = [Laptop("Hp","i7","8gb"),
       Laptop("Lenovo","i5","32gb"),
       Laptop("Dell","i9","16gm")]
print(sorted(com1, key=lambda x:x.ram))

# 9. Write a python program to create a School class and 3 instance variables and 1 class variable.
class School:
    def __init__(self,name,age,std):
        self.name = name
        self.age = age
        self.std = std
    def show(selfs):
        print(selfs.name,selfs.age,selfs.std)
        
school1 = School("Niket",20,15)
school1.show()
# 10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize
#  instance object variables. Also define instance methods to input fields and display field values
class employee:
    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    def show(selfs):
        print(selfs.empid,selfs.name,selfs.salary)
        
employee1 = employee(123,"Niket",15000)
employee2 = employee(13,"Aman",215000)
employee3 = employee(3123,"Vinit",315000)
employee4 = employee(1123,"Rahul",2115000)
employee5 = employee(12533,"Saurav",615000)
employee1.show()
employee2.show()
employee3.show()
employee4.show()
employee5.show()
        