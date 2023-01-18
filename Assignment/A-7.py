# 1. Write a python script to display the number of days in a given month number.
a = int(input("enter the month number"))
match a : 
    case 1 :
        print("31 days")
    case 2 :
        print("28/27 days")
    case 3 :
        print("31 days")
    case 4 :
        print("30 days")
    case 5 :
        print("31 days")
    case 6 :
        print("30 days")
    case 7 :
        print("31 days")
    case 8 :
        print("31 days")
    case 9 :
        print("30 days")
    case 10 :
        print("31 days")
    case 11 :
        print("30 days")
    case 12 :
        print("31 days")

# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
a = int(input("enter the num1"))
b = int(input("enter the num2"))
op = input(("which operator would you like to per for:+,-,/,*:"))
match op :
    case '+' :
      print("the number of addition:",a+b)
    case '-' :
        print("the subtraction of a number is :",a-b)
    case '*' :
        print("the multiplication of number is :",a*b)
    case '/' :
        print("the division of a number is :",a/b)

''' 3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit. '''
triangletype = input("enter the type of triangle you want e.g (iso,right,equ):")
print("enter the three side of a triangle:")
a = int(input("enter first side"))
b = int(input("enter the second side:"))
c = int(input("enter the third side:"))

match triangletype :
    case 'iso' :
        if a == b != c or a != b == c and a != b or a == c:
            print('it is an iso')
        else :
            print('it is not an iso')
    case 'right' :
        if c**2 == a**2 + b**2 :
            print("it is an right angle tringle")
        else :
            print("it is not an right angle triangle")
    case 'equ' :
        if a == b == c :
                 print('it is an equ')
        else :
            print('it is not an equ')

'''4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.'''
age = int(input("enter your age:"))
match age :
    case _ if age <= 10 :
        print("you are a kid")
    case _ if 10 < age <= 20 :
        print("you are a teen")
    case _ if 20 < age <= 40 :
        print("you are a young")
    case _ if 40 < age <= 60 :
        print("you are a experinced")
    case _ if age >=60 :
        print("you are a senior")

'''5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''
a = int(input("enter the number"))
match a :
    case _ if a%2 == 0 :
        print("it is even so : prateek jain")
    case _ if a%2 != 0 :
        print("it is positive odd so : Aditya Chaoudhary")

'''6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement'''
a = "niket play football"
match a:
    case _ if 'niket' == a:
        print("it has a single word")
    case _ if 'niket play football' == a:
        print("it has multi word")

'''7. Write a python program to check whether a given number is positive, negative or
zero using match case statement'''
a = int(input("enter num1"))
b = int(input("enter num2"))
c = int(input("enter num3"))
match a,b,c :
    case _ if a > 0 :
        print("it is positive")
    case _ if a < 0 :
        print("it is negative")
    case _ if a==0 :
        print("it is zero")

'''8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''
a = input("enter a name ")
b = input("enter b name ")
match a,b:
    case _ if a>b :
          print("a come first")
    case _ if a<b :
        print("b come first")
    case _ if a==b :
        print("both are same")

'''9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year'''
a = int(input("enter the year"))
checks = input("type 'all':")
match checks :
    case 'all' :
        if a%100 == 0 and a%400 == 0 :
            print("it is century leap year")
        elif a%100 == 0 and a%400 != 0 :
            print("it is century non leap year")
        elif a%100 != 0 and a%400 != 0 :
            print("it is non century and non leap year")
        else :
            print("non century leap year")
            
'''10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''
print("type which color you like it will display as days of color e.g : red,yellow,blue,orange,white,black,all")
a = input("which color you like : ")
match a :
    case 'red' :
        print("Red-saturday")
    case 'yellow' :
        print("Yellow - Monday")
    case 'orange' :
        print("Orange - Wednesday")
    case 'blue' :
        print(" Blue - Tuesday")
    case 'black' :
        print(" Black - Friday")
    case 'white' :
        print("White - Thursday")
    case 'all' :
        print('All other colours - Sunday')




    
        
        
      
