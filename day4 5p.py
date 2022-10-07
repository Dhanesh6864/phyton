string =str(input("enter the string")) 
print ("The original string  is : ",string)   
reverse_String = ""  
count = len(string) 
while count > 0:   
    reverse_String += string[ count - 1 ] 
    count = count - 1
print ("The reversed string using a while loop is : ",reverse_String)
