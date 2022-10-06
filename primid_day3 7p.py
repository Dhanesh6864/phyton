r=int(input("number of rows"))
k = (2 * r) - 2
for i in range(0, r):
    for j in range(0, k):
        print(end=" ")
    
    k = k - 1
    
    for j in range(i,0,-1):
        print(j, end=' ')
    print(" ")
