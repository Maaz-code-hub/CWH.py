# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


# # fibonacci series
# def fibbonacci(n):
#     if n==0:
#         return 0
#     elif n==1: 
#         return 1
#     else:
#         return fibbonacci(n-1)+fibbonacci(n-2)
    
 
# print(fibbonacci(12))




#  fibonacci series in range
def fibbonacci(n):
    if n==0:
        return 0
    elif n==1: 
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
    
 
n=int(input("Enter the value of n : "))
print(f"The first {n} terms of fibonacci series are :  ")
for i in range(0,n+1):
    print(fibbonacci(i),end="   ")
