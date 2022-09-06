def check(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        

s1 =input('enter 1st string')
s2 =input('enter 2nd string')
check(s1, s2)
