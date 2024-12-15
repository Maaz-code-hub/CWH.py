# #Union
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# #union and update
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)
# print(cities)

# #Intersection
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# #Intersection and update
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# #Symmetric difference
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# #symmetric difference and update
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# #difference
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.difference(cities2)
# print(cities3)

# #difference update
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2)) 





# #disjoint
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))


# #issuperset
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# #subset
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid",}
# print(cities2.issubset(cities))

# #add
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# #update
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2)
# print(cities)

# #remoce/discard
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# #pop
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

# #del
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)
# #throws erros while printing

# #clear
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

#Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")





####The method related to sets are:-
# 1) union()---->creates a new set with the unique elements from both the sets
# 2)update()----->applied on a set itself and it also adds unique elements from the both the sets into one of the sets
# 3) intersection()----> creates a new set with the common elements from both the sets
# 4)intersection_update()------> applied on a set itself and it also contains the common elements from both the sets
# 5)symmetric_difference--------> creates a new set with the elements from the both the sets that are not common in between
# 6)symmetric_difference_update-------> applied on a set itself and it contains elements from the sets that are not common inj between
# 7)difference------> creates a new set with the elements from a single set that are not common 
# 8) difference_update-----> applied on a set itself and contains elements of a set that are not common

# 9)isdisjoint()---->checks if there are common elements between two sets
# 10)issuperset----> checks if a set is a superset of another set
# 11) issubset-----> checks is a set is subset of another set
# 12)add------> to add a element into a set
# 13) remove-------> to remove an elements from a set, but raises key error if the element is not present in the set
# 14) discard-----> to remove an element from a set, does not raises error if the lement is not present in the set
# 15) del------> not method, a keyword, to delete the complete set
# 16) clear-------> to clear all the elements of a set 
# 17) in keyword used to check if a element is present in the set or not
# 18) pop()-----> to remove a random element from the set and also we can get that element

