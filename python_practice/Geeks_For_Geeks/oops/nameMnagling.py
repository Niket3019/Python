class Student:
    def __init__(self,name):
        self.__name = name
acess = Student("Rohit")
print(dir())
print(acess._Student__name)