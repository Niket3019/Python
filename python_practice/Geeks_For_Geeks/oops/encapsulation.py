class Person:
    
    def __init__(self,Age) :
        self.age = Age
    def control(self):
        list1 = ["Niket","Rahul","Saurav"]
        name = input("enter you name")
        if name in list1:
            return f"{self.age} \ncongratulation!!"
        else:
            return "not granted your request!"
p1 = Person(20)

print(p1.control())
        