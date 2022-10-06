year=int(input('Enter the Year: '))
leap=year
if (year%400==0) and (year%100!=0):
  print(year,"is a leap year")
elif (year%4==0):
  print(year,"is a leap year")
else:
    print(year," is not a leap year")
    leap=year-1==year%4 or year-2==year%4 or year-3==year%400 or year-4==year%400
    if(leap==false):
        
        print("leap year",leap-1)
