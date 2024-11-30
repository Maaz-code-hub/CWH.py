fruit = "mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])    #including 0 but not 4
print(fruit[1:4])    #including 1 but not 4
print(fruit[:5])   
print(fruit[0:5])    
print(fruit[0:len(fruit) - 3])   #[0:(5-3)=2]-->[0:2]
print(fruit[-3:-1])              #[len(fruit)-3:len(fruit)-1] -->[2:4]

# Quick quiz
nm = "Harry"
print(nm[-4:-2])           #-->[1:3]  ---> ar