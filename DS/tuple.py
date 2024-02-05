tuple = ("python",9,"learning",1)
tuple1 = (4, "sdf","dsf",78)
print(tuple)
print(tuple[2:])
print(tuple+tuple1)
a,b,c,d = tuple
print(a, b,c,d)
even_square = (x ** 2 for x in range(1, 11) if x % 2 == 0)
print(even_square) #end up as a generator. bcoz tuples are immutable and it doesn't make much sense to have a tuple comprehension that results in a new tuple for each operation.
a = (1,2)
b = (1,2)
print(id(a), id(b))
print(a is b)
print(a == b)