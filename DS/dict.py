dict = {None:"", 2:None,None:None}
print(dict)
dict = {1:"python",2:"learning",3:2.47,'name':"pradeep",'NAME':"PRADEEP","tpl":(1,5,2),"lst":[3,5,8]}
print(dict)
dict1 = dict.copy()
print(dict1)
dict1.clear()
print(dict["name"])
dict.update({"name":56})
print(dict)
dict.pop("NAME")
print(dict)
dict.popitem()
print(dict)
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {k: ('old' if v > 40 else 'young') for (k,v) in original_dict.items()}
print(new_dict)
empList = ['Alex', 'Harry', 'Chris', 'Andy', 'trump']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
temperature = ['30.4', '29', '39.2', '34.1', '38.6', '40', '41.9']
#{key: value for vars in iterable}
print({d:t for (t,d) in dict.items()})
resultLst = {d: t for (d, t) in zip(days, temperature)}
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
new_dict = my_dict
print(new_dict)
print(id(my_dict), id(new_dict))

import copy

# Dictionary
original_dict = {'key': ['value1', 'value2']}
shallow_dict = copy.copy(original_dict)
deep_dict = copy.deepcopy(original_dict)

# Set
original_set = {1, 2, 2, (3, 4)}  # Mutable elements not allowed
shallow_set = copy.copy(original_set)
deep_set = copy.deepcopy(original_set)

# Tuple
original_tuple = (5, 6, ['value1', 'value2'])
shallow_tuple = copy.copy(original_tuple)
deep_tuple = copy.deepcopy(original_tuple)

original_dict['key'].append('value3')
original_tuple[2].append('value3')

print("Original:", original_dict, original_set, original_tuple)
print("Shallow:", shallow_dict, shallow_set, shallow_tuple)
print("Deep:", deep_dict, deep_set, deep_tuple)

