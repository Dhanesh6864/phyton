a=int(input("Enter the no of elements:"))
b=[]
for i in range(a):
    c=float(input("enter the number:"))
    b.append(c)
print("list of elements:")
f={}
for item in b:
    if item in f:
        f[item]+=1
    else:
        f[item]=1
print(f)
print("_________________________")
print('| element  |   frequency  |')
print("-------------------------")
for i in range (a):
    print( "|",b[i],"   |     ",f,"|")
print("_________________________")
