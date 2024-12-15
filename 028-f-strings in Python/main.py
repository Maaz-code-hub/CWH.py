letter = "Hey my name is {1} and I am from {0}"
country= "India"
name="maaz"
# print(letter.format(name,country)) 
# print(letter.format(country,name)) 
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f string like this : Hey my name is {{name}} and I am from {{country}}")

price = 29.088755
txt = f"For only {price: .2f} dollars"
print(txt)