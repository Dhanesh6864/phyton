try:
    num=int(input("enter the number"))
    reversed_num=0
    while num!=0:
        digit=num%10
        reversed_num=reversed_num*10+digit
        num//=10
    print("mirror image:"+str(reversed_num))
except ValueError:
    print("no special chaaters allowed only numbers are allowed")
    
