s=str(input("Enter the string"))
v=0
c=0
s.lower()
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v=v+1
       
    else:
        c=c+1

print("vowels:",v[i])
print("constants:",c[i])
