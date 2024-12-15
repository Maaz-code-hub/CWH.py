#else only executes if loop is completely executed
#else with for loop
for i in range(6):
    print(i)
    if i==4:
        break

else:
    print("Sorry no i")


#else with while loop
i = 0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break

else:
    print("Sorry no i")