# region NON-Primitive - SETS Concept
# SETS are mutable and can hold unique values

def sets_of_fruits():
    fruits = {'apple', 'banana', 'pineapple', 'pear', 'orange', 'apple', 'orange'}
    return fruits


setsOfFruits = sets_of_fruits()
print(setsOfFruits)

# Unions | (Excludes duplicates) returns a set that contains all items from both sides
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # using operator --> Output: {1, 2, 3, 4, 5}
print(a.union(b))  # using method --> Output: {1, 2, 3, 4, 5}

# Intersection & (common elements from both sides)
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # using operator --> Output: {3}
print(a.intersection(b))  # using method --> Output: {3}

# Symmetric Difference - Returns a set that contains all items from both sides except intersection
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)  # using operator --> Output: {1, 2, 4, 5}
print(a.symmetric_difference(b))  # using method --> Output: {1, 2, 4, 5}
set1 = set([1,2,"python",4,"learning",1,"python"])
print(set1)
set1.add("incubation")
print(set)
print("python" in set1)
set2 = set(["this",1,"is",54,"new set"])
print(set2.union(set1))
numbers = {1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8, 8}
print(numbers)
unique_squares = {number**2 for number in numbers}
print(unique_squares)
set1 = {1,2}
set2 = {1,2}
print(id(set1), id(set2))
print(set1 is set2)
print(set1 == set2)
lstst = {1,"ds",(1,2,"asd",5)}
print(lstst)
#lstst = {1,"ds",[1,2,"asd",5]} -> generate TypeError: unhashable type: 'list'
L = (1,2,3)
L1 = L
L1.remove(2)
print(L)
print(L1)
