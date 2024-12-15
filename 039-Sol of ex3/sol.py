import sys
prize=0
name=input("Enter your name : ")
print("Welcome ",name)
question=["1. What is the correct way to create a variable in Python?","2. Which of the following is a valid data type in Python?","3. What does the len() function do in Python?","4. What is the purpose of the if statement in Python?","5.What is the correct way to create a comment in Python?"]
options=["1. var x = 10\n 2. x := 10\n 3. x = 10\n4. int x = 10","1. int\n 2. char\n3. float\n4. Both 1. and 3.","1. Calculates the length of a number.\n2. Returns the length of a string, list, or otheriterable.\n3. Converts a string to lowercase.\n4. Finds the largest number in a list.","1. To create a loop.\n2. To handle errors in the program.\n3. To execute a block of code only if a specified condition is true.\n4. To define a function.","1. // This is a comment\n2. /* This is a comment */\n3. # This is a comment\n4. <!-- This is a comment -->"]
correctopt=[3,4,2,3,3]
for  i in range(0,5):
    print(question[i]) 
    print(options[i])
    ans = int(input("Chose the above options(1-4):\n "))
    if(ans!=correctopt[i]):
        print("Wrong ans !!\nOUT of game")
        print("Total prize won = ",prize)
        sys.exit(0)
    else:
        prize=prize+500
        print("Total prize won = ",prize)
        
