import copy
import random





# endregion

# region NON-Primitive - LIST Concept

lst = [1, 2, 3]
other = ['a', 'b', 'c']
lst.extend(other)
print(lst)  # Output: [1, 2, 3, 'a', 'b', 'c']

lst = [1, 2, 3, 4, 5]
lst.remove(4)
print(lst)  # Output: [1, 2, 3, 5]
lst.remove(5)
print(lst)  # Output: [1, 2, 3, 5]

lst = [1, 2, 3, 'a', 'b', 'c']
print(len(lst))  # Output: 6

lst = [1, 3, 2, 4, 5]
lst.sort()
print(lst)  # Output: [1, 2, 3, 4, 5]

li1 = [1, 2, [3, 5], 4]
li3 = copy.deepcopy(li1)
print("li3 Value: ", li3)

lit = [1.2, 1.3, 0.1]
max_value = max(lit)
print(max_value)

names = ["mariya", "BATMAN", "abidance"]
names = [name.upper() for name in names]
print(names)

bool_list = [True, False, False, True, False, False, True, True]
to_bits_list = [1 if b is True else 0 for b in bool_list]
print(bool_list)
print(to_bits_list)

my_string = "HelloMyNameIsNazim"
# my_string = "".join([i if i.islower() else " " + i for i in my_string])[1:]
# print(my_string)
my_string = "".join([i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i
                     for i in my_string])[1:]
print(my_string)
print(names.count("BATMAN"))
del names[0:2]
print(names)
# endregion

# region DICTIONARY Concept
# A dictionary is an unordered collection of data values that can be used to store data values

Dict1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict1.keys())
print(Dict1.values())
print("Dictionary:")
print(Dict1[1])

# overrides a from 1 to 100
xdict = {'a': 1, 'b': 2, 'a': 100}
print(xdict)

xdict['d'] = 200
print(xdict)

for (key, val) in xdict.items():
    print('Key is:', key, 'Value is:', val)

# nested dictionary using for loop
a = {1: {'course': 'Python', 'fees': 15000},
     2: {'course': 'Dotnet', 'fees': 14000}}

print("ID")
for ids in a:
    print(ids)
print()

for ids in a:
    for k in a[ids]:
        print(k, '=', a[ids][k])
print()


# 2 Dictionaries Merging
def merge():
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    dict2.update(dict1)
    return dict2


print('merging 2 dicts: ', merge())

# endregion

# region LIST Comprehension (in single line, it creates list)
lst1 = [('EPAM' + str(i + 1)) for i in range(20)]
print(lst1)

# appends i only when i%2 == 0
lst2 = [i for i in range(20) if i % 2 == 0]
print(lst2)

lst3 = [i for i in range(20) if i % 2 == 0 if i % 3 == 0]
print(lst3)


# endregion

# region SWITCH Case
# Function to convert number into string
# Switcher is dictionary data type here


def numbers_to_strings(arg):
    switcher = {
        0: "zero",
        1: "one",
        2: "two"
    }
    print(type(switcher))
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(arg, "nothing")


argument = 0
print(numbers_to_strings(argument))

argument = 3
print(numbers_to_strings(argument))
# endregion

# region DICTIONARY Comprehension

empList = ['Alex', 'Harry', 'Chris', 'Andy', 'trump']

dict_arr = {emp: random.randint(1, 100) for emp in empList}
print(dict_arr)

# endregion

# region DICTIONARY Comprehension using ZIP

# Note: The zip function takes in a sequence of iterables as the argument,
#   and returns an iterator of tuples, as shown in the image below.
# List is iterable
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
temperature = ['30.4', '29', '39.2', '34.1', '38.6', '40', '41.9']

resultLst = {d: t for d, t in zip(days, temperature)}
print(resultLst)

resultLst1 = {k: v for k, v in zip(empList, ([i for i in range(5)]))}
print(resultLst1)

names = ['Harry', 'Hermione', 'Ron', 'Neville', 'Luna']
index = {k: v for (k, v) in enumerate(names)}
print(index)
# Output {'Harry': 0, 'Hermione': 1, 'Ron': 2, 'Neville': 3, 'Luna': 4}

my_dict = {"Spider": "Doctor", "Bat": "Philanthropist", "Wonder wo": "nurse"}
my_dict = {(key + "man" if key != "Spider" else key):
               (value if value != "Doctor" else "Journalist")
           for (key, value) in my_dict.items()}
print(my_dict)

# endregion

# region DICTIONARY Final Exercise

bases = ["A", "T", "C", "G"]
strand1 = random.choices(bases, k=10)
print(strand1)

dna = {key: [val, ("T" if val == 'A' else "A" if val == 'T' else "C" if val == "G" else "G")]
       for (key, val) in enumerate(strand1)}
print(dna)

list_emp = ["EPAM1", "EPAM2", "EPAM3", "EPAM4"]
list_emp = {val: key for (key, val) in enumerate(list_emp)}
print(list_emp)
# endregion


# region LAMBDA
# sorting using custom key
employs = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

employs.sort(key=lambda x: x.get('Name'))
print(employs, end='\n\n')
employs.sort(key=lambda x: x.get('Name'), reverse=True)
print(employs, end='\n\n')


# endregion

# *Args and **Kwargs
def check(z, y, *args, d=4, f=5, **kwargs):
    print(f'{z} - {y} - {args} - {d} - {f} - {kwargs}')


check(2, 4, 5, 5, f=10, d=15, k=45, o=87)
check(2, 4, 2, 4, 5, 6, k=45, o=87, f=10, d=19)

tuple_collection = (1, 'Help', 2, 'EPAM', 3, 'Sphere', 4, 'Arrow')
print(tuple_collection[0:8:2])
print(tuple_collection[-1:-8:-2])
print(tuple_collection[-2:-9:-2])

languages = ['Python', 'Java', 'JavaScript']
temp = enumerate(languages)
temp1 = enumerate(languages)
print(list(temp))
print(dict(temp1))

lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lit[-1:-6:-4])
print(lit[-1:-6:-4])
print(lit[9:-6:-4])
print(lit[-1:2:-4])

print(lit[0:9:2])

