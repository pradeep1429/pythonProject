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
print(id(L), id(L1))
print(L is L1)
print(L == L1)
a = [1,2]
b = [1,2]
print(id(a), id(b))
print(a is b)
print(a == b)

L = [[1,2,3],[4,5,6],[7,8,9]]
print([indiv for inner in L for indiv in inner])
print(type(L))
print(type(L).__name__)
print([y for x in L for y in x]) #[expression for item in iterable]
nl = [1, 2, [3, 4, 5, 6 ], 7, 8, [9, 10 ] ]
print([indiv for inner in nl for indiv in (inner if isinstance(inner, list) else [inner])])
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
x=1
y=1
z=2
n=3
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])
# res = []
# for a in range(x+1):
#     for b in range(y + 1):
#         for c in range(z + 1):
#             if(a+b+c != n):
#                 res.append([a,b,c])
#
# print(f"final list: {res}")
#[[1,1,1],[2,2,2],[3,3,3]]
print([[a,b,c] for a in range(1,4) for b in range(1,4) for c in range(1,4) if a==b==c])
print([[i]*3 for i in range(1, 4)])
#[[1,0,0],[0,2,0],[0,0,3]]
print([[i if inner == outer else 0 for inner in range(3)] for outer,i in enumerate(range(1,4))])

students_dict = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41.0, 'Harsh': 39.0}
second_lowest_names = []
# Getting all the unique grades and sorting them
grades = sorted(set(students_dict.values()))

# Getting the second lowest grade
if len(grades) >= 2:
    second_lowest_grade = grades[1]
else:
    second_lowest_grade = grades[0]

# Collecting students who have the second lowest grade
for student, grade in students_dict.items():
    if grade == second_lowest_grade:
        second_lowest_names.append(student)

# Sorting names in alphabetical order
second_lowest_names.sort()

# Printing names line by line
for name in second_lowest_names:
    print(name)


student_marks = {"harsh":[25,26.5,28]}

l = student_marks.get('harsh')
add = 0
for i in range(0,len(l)):
    add = add + l[i]
res = add/len(l)
print(f"{res:0,.2f}")

list = [ [ ] ] * 2
print(list)
list[0].append(10)
print(list)
list[1].append(20)
print(list)
list.append(30)
print(list[0])


def function(nums):
  for i in range(len(nums)):
        x =abs(nums[i]-1)
        if(nums[x]<0):
            return x+1
        else:
            nums[x] = -nums[x]

print(function([1,2,3,1,2]))

numbers = [1, 3, 4, 2, 5, 6, 8, 7, 9]

highest = second_highest = float('-inf')
print(highest)









