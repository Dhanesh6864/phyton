m=int(input("how many numbers do you enter:"))
n=()
for i in range (0,m):
    n= int(input(""))
print(n)
for i in range (n[i],n[i+1]):
    if(n ==0 or n == 1):
        printf(n,"Number is neither prime nor composite")
    elif n>1 :
          for i in range(2,n):
              if(n%i == 0):
                  print(n,"is not prime but composite number")
                  break
              else:
                   print(n,"number is prime but not composite number")
    
    else :
        print("Please enter positive number only ")
