# a = int(input("Enter any value between 5 and 9 : "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

##Quick quiz
#if user entered "quiz" or any integer error should not occur.in reat all cases error should occor
a = input("Enter the value (quit/between 5 to 9): ")

# Check if input is not "quit" and not between 5 and 9
if a != "quit":
    try:
        # Convert to integer and check the range
        value = int(a)
        if value < 5 or value > 9:
            raise ValueError("Not a valid input !!")
    except ValueError:
        raise ValueError("Not a valid input !!")
else:
    print("Exiting...")
    exit()

print(a)
