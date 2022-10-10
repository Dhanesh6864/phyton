python=int(input("Enter your marks in Python:"))
c=int(input("Enter your marks in C programming:"))
maths=int(input("Enter your marks in Mathamatics:"))
physics=int(input("Enter your marks in Physics:"))
total=python+c+maths+python
print("Your total marks is:",total)
avg=total/4
print("Your Aggregrate marks is:",avg)
if(avg<=100 or avg>95):
    print("Your grade is S")
elif(avg<=95 or avg>90):
    print("Your grade is A")
elif(avg<=90 or avg>80):
    print("Your grade is B")
elif(avg<=80 or avg>70):
    print("Your grade is C")
elif(avg<=70 or avg>60):
    print("Your grade is D")
elif(avg<=60 or avg>50):
    print("YOur grade is E")
else:
    print("You are FAIL")
