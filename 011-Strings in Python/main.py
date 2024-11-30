# what is string
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode charact

name="maaz"

# How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

# we usually use single quotes('xyz')when we have a statement consisting of double quote("xyz") and vise versa(we can also use \' or \")
# example

print("He said, 'I want to eat an apple'.")
print('He said, "I want to eat an apple".')

#multiline string(using triple double quote/single quote)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# string is like a array
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])   #throw an error because invalid location(4)
print("lets use for loop\n")
for character in a:
    print(character)
