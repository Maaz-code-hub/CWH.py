import math
result1=math.sqrt(9)*math.pi
print(result1)

from math import sqrt,pi       #imort perticular options
result2=sqrt(9)*pi
print(result2)

# from math import *         #Imports all the functions of math module import all names (functions, variables, constants) (not recomemded)
# result3=sqrt(9)*pi
# print(result3)

import math as m                #can be used in all the above and below cases except in *
result4=m.sqrt(9)*m.pi
print(result4)


# import math
# print(dir(math))                  #print all the function varriables in math module


# Create your module
# all the other methods can be used for importing
import maaz

maaz.welcome()
print(maaz.mk)