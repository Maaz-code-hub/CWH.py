# def average(a=9,b=9):
#     print("The average is ",(a+b)/2)

# # average(4,6)
# average(1,5)



def avg(*numbers):
    # print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum + i
    # print("The avg is ",sum/len(numbers))
    return sum/len(numbers)
    

c = avg(1,3,5,5)
print(c)




# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")