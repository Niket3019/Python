# print add of two variable
a = 75
b = 27
c = a+b
print(c)

# print new line with sep 
a = 7344
b = "niket"
c = True
print(a,b,c,sep="\n")
print(a,b,c,end="000")
print(b*5,sep="\n")

# Many Values to Multiple Variables
a,b,c = "Niket","Rahul","Saurav"
print(a,b,c,sep="\n")

# Unpack a Collection
name = ["niket","rahul","saurav"]
d,e,f = name
print(d,e,f,sep="\n")

# One Value to Multiple Variables
name = "Niket"
x = y = z = name
print(x,y,z,sep="\n")
print(id(x))

# Global Varibale 
name1 = "Niket"
def myfunc():
   name1 = "Ronak"
   print(name1)
myfunc()
print(name1)

# practice
a = input("enter your name ")
print(a,"you are eligible")

