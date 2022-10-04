def count_chars(str):
    u,l,n,s=0,0,0,0
    for i in range (len(str)):
        if str[i]>='A' and str[i]<='Z':u+=1
        elif str[i]>='a' and str[i]<='z':l+=1
        elif str[i]>='0' and str[i]<='9':n+=1
        else: s+=1
    return u,l,n,s
str=input("enter any sub strings")
u,l,n,s=count_chars(str)
print("upper case charaters are:",u)
print("lower case charaters are:",l)
print("number of cases are :",n)
print("special case charaters are:",s)
