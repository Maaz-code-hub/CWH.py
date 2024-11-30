# strings are immutable
a = "  Maaz!!!  "
print(len(a))
print(a.upper())                     #This method does not chage the orginal string
print(a.lower())
print(a.strip())                     #The strip() method removes any white spaces before and after the string
str3 = "Hello !!!"
print(str3.rstrip("!"))              #the rstrip() removes any trailing(end) characters
print(a.replace("Maaz","Furqan"))    #The replace() method replaces all occurences of a string with another string.
print(a.split(" "))                    #The split() method splits the given string at the specified instance and returns the separated strings as list items.
bloghead = "hello coders"
print(bloghead.capitalize())         # The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase