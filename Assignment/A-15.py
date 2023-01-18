# 1. Write a python script to create a String in 3 different possible ways
a,b,c = "Niket",'''Niket''','Niket'

# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
a = "iNeuron"
print(a[ :6])

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
a = "Hello Learners"
print(a[2:6])

# 4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )
a = "Learning"
b = "Python"
c = " ".join([a,b])
print(c)

# 5. Write a python script to get the count of total number of characters in String a= “iNeuron”
a = "iNeuron"
count = 0
for i in a :
    if type(a) == str:
        count+=1
        print(count) 

# 6. Write a python script to reverse a String. (“iNeuron”)
a = "iNeuron"
print(a[7::-1])

# 7. Write a python script to determine whether a string contains a specific substring
a = "i have an apples"
b = a.split()
print(b)

if 'apples' in b:
        print("it has substring")
else:
        print("it not has substring")

# 8. Write a python script to check if a string contains only numbers
a = (input("enter a any num or value"))
if a.isdigit():
    print("all value conatin number")
else:
    print("it dosen't contain number")

# 9. Write a python script to check if a string contains only characters of the alphabet.
a = (input("enter a any num or value"))
if a.isalpha():
    print("all value conatin alpha")
else:
    print("it dosen't contain alpha")
    
# 10. Write a python script to convert an integer to a string.
a = 23674
b = str(a)
print(b)
