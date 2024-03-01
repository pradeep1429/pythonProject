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

dict_comp = {  "count": 24,  "players": [    {      "id": 439,      "name": "David de Gea",      "position": "Keeper",      "jerseyNumber": 1,      "dateOfBirth": "1990-11-07",      "nationality": "Spain",      "contractUntil": "2019-06-30",      "marketValue": None    },    {      "id": 440,      "name": "Sergio Romero",      "position": "Keeper",      "jerseyNumber": 20,      "dateOfBirth": "1987-02-22",      "nationality": "Argentina",      "contractUntil": "2018-06-30",      "marketValue": None    },    {      "id": 441,      "name": "Eric Bailly",      "position": "Centre-Back",      "jerseyNumber": 3,      "dateOfBirth": "1994-04-12",      "nationality": "Cote d'Ivoire",      "contractUntil": "2020-06-30",      "marketValue": None    }  ]}
spain_players = [player for player in dict_comp['players'] if player['nationality'] == "Spain"]
print(spain_players)
print(dict_comp['players'][0].get('nationality'))

users = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
print([user for user in users['data'] if user['email']=='tobias.funke@reqres.in'])
print({user['id']:user['email'] for user in users['data']})