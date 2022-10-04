a=float(input("enter the string number"))
b=int(input("max no of lines to be printed"))
for i in range(b):
    for j in range(i+1):
        print('%2.f'%a,end=' ')
        a=a+0.1
    print()
    

