marks = [3,5,6,"maaz",True,6,7,2,32,345,23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])


# # Negative indexing method 1
# print(marks[-3]) #negative indexing
# print(marks[len(marks)-3]) #negative index to positive index
# print(marks[5-3]) #positive index
# print(marks[2]) #positive index



# # Negative indexing method 2
# print(marks[-3]) #negative indexing
# # marks[-3] means that the 3rd term from last i.e,6


# if 7 in marks:
#     print("yes")
# else:
#     print("No")

# #Same thing apply for string
# if "ha" in "harry":
#     print("yes")

# print(marks)
# print(marks[:]) #print all
# print(marks[1:8])
# print(marks[1:8:2])

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)