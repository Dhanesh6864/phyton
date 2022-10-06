def perfectSquares(l, r):
    for i in range(l, r + 1):
        if (i**(.5) == int(i**(.5))):
            print(i, end=" ")
l=int(input("enter the starting range="))
r=int(input("enter the ending range="))
 
perfectSquares(l, r)
