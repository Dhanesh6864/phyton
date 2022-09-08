rows=int(input("enter the number of rows:"))
for i in range(0,rows):
    print(" ")
    for j in range(0,i+1):
        print(i+1,end=" ")
    print("\r")
