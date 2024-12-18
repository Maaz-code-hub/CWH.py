def code():
    n = input("Enter the word to be coded : ")
    if(len(n)>=3):
        n=n+n[0]
        n=n.replace(n[0],"")
        n="pqr"+n+"abc"
        print(n)
    else:
        print(n[::-1])

def decode():
    n = input("Enter the word to be decoded : ")
    if(len(n)>=3):
        n=n.replace("abc","")
        n=n.replace("pqr","")
        n=n[-1]+n
        print(n[:-1])
        
    else:
        print(n[::-1])

a=int(input("1 For code and 2 For decode : "))
if a==1:
    code()
elif a==2:
    decode()
else:
    print("Invalid input!!!")


# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
