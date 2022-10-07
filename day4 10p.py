s =str(input("enter the string")) 
print ("The original string  is : ",s)   
reverse_String = ""  
count = len(s) 
while count > 0:   
    reverse_String += s[ count - 1 ] 
    count = count - 1
print ("The reversed string using a while loop is : ",reverse_String)
