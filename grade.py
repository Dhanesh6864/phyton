print("Enter Marks Obtained in 3 Subjects: ")
phyton = int(input())
java = int(input())
cprogramming = int(input())

tot = phyton+java+cprogramming
avg = tot/3

if avg>=81 and avg<=100:
    print("Your Grade is A")
elif avg>=61 and avg<80:
    print("Your Grade is B")
elif avg>=51 and avg<60:
    print("Your Grade is c")
elif avg>=40 and avg<50:
    print("Your Grade is d")
 
else:
    print("fail")
