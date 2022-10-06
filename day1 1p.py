try:
    a=int(input("enter the no of fresh loaves:"))
    b=int(input("enter the no of old loaves:"))
    c=a*185
    d=b*185*0.6
    print("the regular price is:185")
    print("amount of new loaves is:",c)
    print("aount of old loaves is:",d)
    print("total amount is:",c+d)
except ValueError:
    print("please enter only positive and without decimal value.")
