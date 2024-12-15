# dic = {
#     "Harry": "Human being",
#     "Spoon":"object"
# }

# print(dic["Harry"])

# dict = {
#     344 : "Harry",
#     56 : "Subham",
#     678 : "Zakir",
#     567  : "Neha"
# }
# print(dict[567])

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# # print(info['name2'])         #throws error if not exits
# # # print(info.get('name2'))   #print none if not exits
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"The values corresponding to the key {key} is {info[key]}")

print(info.items())
for key,value in info.items():
    print(f"The key is {key} and its corresponding value is {value}")