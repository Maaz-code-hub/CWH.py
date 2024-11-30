# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

# SYNTAX-->variable=input()

# eg-->variable=int(input())
#      variable=float(input())


a=input("Enter your name:")   
print("your name is-->",a)

x=input("enter first number:")    #Taken a is x string
y=input("enter second number:")   #Taken a is y string
print(x+y)                        #string 1 + 1=11
print(float(x)+int(y))            #typecasting(changing type)


# we can also first declare the type of input
# example is given below
m=int(input("enter the value of m:")) 
n=int(input("enter the value of n:"))
print("m+n=",m+n) 