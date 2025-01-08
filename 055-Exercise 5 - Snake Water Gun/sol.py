import random as r
cmp=r.randint(0,2)
user=int(input("Enter 0 for snake\n1 for water\n2 for gun\n"))
print(f"cmp is {cmp}")
print(f"user is {user}")
if(user==cmp):
    print("Draw")

elif(cmp==0 and user ==1)or(cmp==2 and user ==0)or(cmp==1 and user ==2):
    print("cmp wins!")
else:
    print("User wins")