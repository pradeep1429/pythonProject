import copy

list1 = ["a","b","c","d"]
print(list1)
list1.append(1)
print(list1)
list1.remove("b")
print(list1)
list1.pop()
print(list1)
list1.sort()
print(list1)
print(list1.count("a"))
list1.reverse()
print(list1)
list1.insert(0,8)
list1.extend(['python','learning',(14,29)])
print(list1)
even_square = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_square)
even_square = tuple(x ** 2 for x in range(1, 11) if x % 2 == 0)
print(even_square)

list1.clear()
print(list1)
lst = [12,4,3,65,23,76,98,34,20,25,50]
print(lst)
print("after slicing: {}".format(lst[5:0:-2])) #[start:end:step]
print("after slicing: {}".format(lst[5::-3])) #::n - every nth element in sequesnce
print("after slicing: {}".format(lst[0:12:3]))
L = [1,2,3]
L1 = L
del L1[2]
print(L)
print(L1)

a = [1,2]
b = [1,2]
print(id(a), id(b))
print(a is b)
print(a == b)

L = [[1,2,3],[4,5,6],[7,8,9]]
print(type(L))
print(type(L).__name__)
print([y for x in L for y in x]) #[expression for item in iterable]
nl = [1, 2, [3, 4, 5, 6 ], 7, 8, [9, 10 ] ]
print([y for x in nl for y in (x if isinstance(x, list) else [x])])
lst = [12,4,3,65,23,{76,98,34},(20,25,50)]
print(lst[6][1:])


original = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
shallow = copy.copy(original)

original[1][0] = 'X'

print(f'original:{original}')    # Output: [[1, 1, 1], ['X', 2, 2], [3, 3, 3]]
print(f'shallow: {shallow}')     # Output: [[1, 1, 1], ['X', 2, 2], [3, 3, 3]]
print(id(original), id(shallow))

original = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
deep = copy.deepcopy(original)

original[1][0] = 'X'

print(f'original:{original}')    # Output: [[1, 1, 1], ['X', 2, 2], [3, 3, 3]]
print(f'deep: {deep}')     # Output: [[1, 1, 1], ['2', 2, 2], [3, 3, 3]]
print(id(original), id(deep))

print([[row+col for col in range(3)] for row in range(5)])
print([[col for col in range(row,row+3)] for row in range(1,15,3)])











