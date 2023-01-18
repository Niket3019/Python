class Student():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def add(self,other):
        total_m1 = self.m1 + other.m1
        total_m2 = self.m2 + other.m2
        print(total_m1,total_m2)
marks1 = Student(12,15)
marks2 = Student(13,14)
marks1.add(marks2)