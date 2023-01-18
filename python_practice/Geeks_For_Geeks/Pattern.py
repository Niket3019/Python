#1
input = int(input("enter a row"))
for i in range(1,input+1):
    print()
    for j in range(1,i+1):
        print("*",end=" ")

#2
input = int(input("enter a row"))
for i in range(1,input+1,2):
    print()
    for j in range(1,i+1):
        print("*",end=" ")

#3
row = int(input("enter a number of row:"))
for i in range(0,row):
    print()
    for j in range(0,row-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")

#4
row = int(input("enter a number of row:"))
for i in range(row,0,-1):
    print()
    for j in range(0,row-i):
        print(end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
  