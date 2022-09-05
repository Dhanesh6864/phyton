import cmath
print("enter values of a,b and c")
a =int(input('a'))
b =int(input('b'))
c =int(input('c'))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
      
