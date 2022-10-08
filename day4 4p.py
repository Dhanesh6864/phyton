t=int(input("total Users"))
s=int(input("staff Users"))
a=0
p=s/3

if(t<=0 or s>=t):
    print("invallied input")
else:
    a=t-(s+p)
    print("student users",a)
