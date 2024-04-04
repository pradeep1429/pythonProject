# write a function which takes two arguments: 1. List of integers; 2. Single integer.
# function should return the indexes of list items, the sum of which is equal to the second argument
# Example: get_sum([1, 23, 19, 7, 3, 10, 9], 8) should return (0, 3)
from collections import Counter


def get_index(list,result):
    tup=()
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if(list[i] + list[j] == result):
                tup = (i,j)
                break
    return tup

print(get_index([1, 23, 19, 7, 3, 10, 9], 32))

#######################################################################
# Sort negative numbers in asc order
# ip = [1, -2, 3, -2, -8, 9, -6]
# op = [1, -8, 3, -6, -2, 9, -2]
ip = [1, -2, 3, -2, -8, 9, -6]
idx = []
for i in range(0,len(ip)):
    if ip[i]< 0:
        idx.append(i)
for i in range(0,len(ip)):
    for j in range(len(idx)-1):
        if ip[idx[j]] > ip[idx[j+1]]:
            ip[idx[j]], ip[idx[j+1]] = ip[idx[j+1]], ip[idx[j]]

print(ip)


#######################################################################
# input: AABCCDD
# output: A2B1C2D2
# input: AAABBCDDA
# output: A3B2C1D2A1
input_str = 'AAABBCDDA'
count_dict = Counter(input_str)

print(count_dict)

def get_count(input):
    all_freq = {}

    for i in input:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print(f"Count of all characters in '{input}' is :\n "
          + str(all_freq))
    count = 1
    result = ''
    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            count += 1
        else:
            result += input[i - 1] + str(count)
            count = 1
    result += input[-1] + str(count)
    print(result)

    for index,c in enumerate(input):
        if input[:index +1].count(c) > 1:
            print(f"first repetetive character is: {c}")
            break
    for index,c in enumerate(input):
        if input[:index +1].count(c) == 1:
            print(f"first non repetetive character is: {c}")
            break

get_count("AACABBCDDAD")
get_count("HelloWorld")
#get_count("Python is a great programming language")
#########################################################################
#dic = {'name':['abc', 'def'], 'edu': ['BTECH', 'BPHARM'], 'city':['hyd', 'ban']}
#output should be : {'name':['ABC', 'DEF'], 'edu': ['btech', 'bpharm'], 'city':['Hyd', 'Ban']}

dic = {'name':['abc', 'def'], 'edu': ['BTECH', 'BPHARM'], 'city':['hyd', 'ban']}
def swap_case(values, type):
    res = []
    for val in values:
        match type.lower():
            case "swap":
                res.append(val.swapcase())
            case "camel":
                res.append(val.capitalize())
    return res

for k,v in dic.items():
    if k.__eq__("city"):
        dic.update({k:swap_case(v, "camel")})
    else:
        dic.update({k: swap_case(v, "swap")})
print(dic)

##############################################################################
# Write fibonacci for given range
a,b = 0,1
while(a<20):
    a,b = b, a+b
    print(a)
# write code for factorial
fac = 1
for i in range(5):
    fac += fac * i
print(f"factorial is {fac}")
##############################################################################
# Write python code for li1 = [1,2,3,4,4,4,5,8] li2=[2,2,3,6,7]
# print common elements from both elements do not use sets.
li1 = [1,2,3,4,4,4,5,8]
li2=[2,2,3,6,7]
res = []
for i in li1:
    if i in li2:
        res.append(i)
print(res)

##############################################################################
# Write code to find the highest element in list
lst = [1,9,-1,0,39,21,13]
highest = lst[0]
for i in lst:
    if i > highest:
        highest = i
print(f"highest: {highest}")

# Write code to find the nth highest element in list
second_high = lst[0]
highest = max(lst)
for i in lst:
    if i!=highest and i > second_high:
        second_high = i
print(f"second highest:{second_high}")
# Write code to find lowest
lowest = lst[0]
for i in lst:
    if i < lowest:
        lowest = i
print(f"lowest: {lowest}")

###############################################################################
def function(nums):
    for i in range(len(nums)):
        x = abs(nums[i] - 1)
        if nums[x] < 0:
            return x + 1
        else:
            nums[x] = -nums[x]

# print(function([4, 3, 2, 7, 8, 2, 3, 1]))
# print(function([2,3,1,6]))
# print(function([3, 4, 2, 1]))
# print(function([2, 3, 1, 0, 2, 5, 3]))
##################################################################################
def nth_highest(numbers, n):
    nth = highest = float('-inf')
    count = 0
    if(n < len(numbers)):
        for num in numbers:
            # If current number is greater than current highest number, update nth, highest and increment count
            if num > highest:
                nth = highest
                highest = num
                count += 1
            # If the current number is less than the highest number,but greater than the nth number, and is not a duplicate,update nth number and increment count
            elif highest > num > nth:
                nth = num
                count += 1
        return nth if count >= n else None


numbers = [55, 34, 13, 36, 6, 36, 33]
n = 2
print(nth_highest(numbers, n))
#################################################################################
lst = [1,2,7,4]
for i in range(len(lst)):
	if i%2 == 0:
		del lst[i]
print(lst)
#################################################################################
# Write code to print triangle pattern
n=5
for s in range(1,n+1):
    print(" *"*s, end="\n")

p=1
for s in range(n,-1,-1):
    print(" "*s+ " *"*p, end="\n")
    p +=1
#################################################################################
# Write code to check given number is armstrong
# 153 = 1*1*1 + 5*5*5 + 3*3*3 - 153 is an Armstrong number.
num = 153
def check_armstrong(n):
    res = 0
    digits = list(map(int, str(n)))
    for d in digits:
        res += d ** len(str(n))
    return res.__eq__(n)

print(check_armstrong(153))
print(check_armstrong(1531))
#################################################################################
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three, print "Fizz" instead of the number,
# for multiples of five, print "Buzz".
# For numbers which are multiples of both three and five, print "FizzBuzz".
for i in range(1,100):
    if i % 3 == 0:
        print(f"{i}-Fizz",end=" ")
    elif i % 5 == 0:
        print(f"{i}-Buzz",end=" ")
    elif i % 3 and i % 5 == 0:
        print(f"{i}-FizzBuzz")
print("\n")
#################################################################################
# Write code for string reverse
var = "pradeep"
chars = [char for char in var]
print("".join(chars[::-1]))
#################################################################################
# Write code to check given number is prime
def check_prime(n):
    flag = False
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                flag = True
                break
    if flag:
        print(f"{n} is not prime")
    else:
        print(f"{n} is prime")

check_prime(15)
limit = 20
prime = ""
for num in range(2,21):
    for i in range(2,num):
        if (num % i) == 0:
            break;
    else:
        print(num,end=" ")

#################################################################################
# Write code using loops to sort a list
l = [5,2,4,9,1]

for i in range(len(l)-1,0,-1):
    for j in range(i):
        if l[j] > l[j+1]:
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
print(l)
#################################################################################
def wrapper(f):
    def fun(l):
        # complete the function
        op = []
        for i in l:
            str_num = str(i)
            if len(str_num)==10:
                op.append(int(str_num))
            elif len(str_num)>10:
                x = str_num[(len(str_num)-10):]
                op.append(int(x))
        op.sort()
        op = ["+91 "+str(i) for i in op]
        f(op)
        return op

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

mob = [7895462130,919875641230,9195969878]
sort_phone(mob)
#################################################################################
# Write code to Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list) // 3
start = 0
end = chunk_size
for i in range(3):
    indexes = slice(start, end)
    list_chunk = sample_list[indexes]
    print(list_chunk)
    start = end
    end += chunk_size

#################################################################################
# L1 = [23, 21, 2, 32, 4, 89, 10, 5, 0, 99, 12]
# 1)Convert above list in dictionary with key as index and value as pairs  , desired o/p-{'0':'23','1':'21','2':'2',......}
# 2)convert above list in dict with key value pair {'23':'21','2':'32','4':'89','10':'5','0':'99'}
L1 = [23, 21, 2, 32, 4, 89, 10, 5, 0, 99]
print({k:v for (k,v) in enumerate(L1)})
print({L1[i]:L1[i+1] for i in range(0,len(L1),2)})

#################################################################################
# Read the string and get the sum of digits, "a5k3k44j808"
input = "a5k3k44j808"
res = 0
for i in range(len(input)):
    if input[i].isdigit():
        res += int(input[i])
print(res)

#################################################################################
#output: [-1,1], [-1,-2,3], [-3,3], [-2,-3,5]

list1 = [-1,-2,-3,1,3,5]
length = len(list1)
sub_lists = []
for i in range(length):
    for j in range(1,length):
        if list1[i] + list1[j] == 0:
            sub_lists.append([list1[i],list1[j]])
        for k in range(2,length):
            if list1[i] + list1[j] + list1[k] == 0:
                sub_lists.append([list1[i], list1[j], list1[k]])

print(sub_lists)

#################################################################################

ls = [10,2,3,4,5,6]
res = []
def max_sum(nums, k):
    sum_list = [sum(nums[i:i+k]) for i in range(len(nums)-k +1)]
    return max(sum_list)

print(max_sum(ls,3))
#################################################################################

list1 = [2,5,8,3,6]
list2 = [1,4,7,2,9]
list3 = (list1 + list2)
# for i in range(len(list3)-1,0,-1):
#     for j in range(i):
#         if list3[j] > list3[j+1]:
#             tmp = list3[j]
#             list3[j] = list3[j+1]
#             list3[j+1] = tmp
while True:
    swapped = False
    for i in range(0,len(list3)-1):
        if list3[i] > list3[i+1]:
            list3[i+1],list3[i] = list3[i],list3[i+1]
            swapped = True
    if not swapped:
        break
print(list3)
#################################################################################
import itertools


def subsets_with_zero_sum(nums):
    subsets = []

    # Generate subsets of different lengths
    for length in range(4):
        # Generate subsets of current length
        for subset in itertools.combinations(nums, length):
            # Only add to results if sum is 0
            if sum(subset) == 0:
                sublist = list(subset)
                if len(sublist).__ne__(0):
                    subsets.append(sublist)

    return subsets


# Test the function
list1 = [-1, -2, -3, 1, 3, 5]
print(subsets_with_zero_sum(list1))


def subsetSum(nums):
    if nums is None:
        return -1
    res = []
    find_subsets(sorted(nums),0,[], res)

def find_subsets(lst, index, path, res):
    if sum(path) == 0 and len(lst) > 0:
        res.append(path)
    for i in range(index,len(lst)):
        find_subsets(lst, i+1, path + [lst[i]], res)

list1 = [-1, -2, -3, 1, 3, 5]
print(subsetSum(list1))
###########################################################################
s = "rescueoperation"
vow = "aeiou"
cur = maxx = ""
all_freq = {}
for c in s:
    if c in vow:
        if c in all_freq:
            all_freq[c] += 1
        else:
            all_freq[c] = 1
        cur+=c
        if len(cur) > len(maxx):
            maxx = cur
    else:
        cur = ""

print(maxx)
print(all_freq)

###########################################################################
l1 = [1,5,3,7,9]
l2 = [2,4,6,8,10, 12,14]
i = 0
j = 0
l3 = []
while i < len(l1) and j < len(l2):
    if l1[i] <= l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1
else:
    l3 = l3 + l1[i:len(l1)] + l2[j:len(l2)]
print(l3)
#############################################################################
def longest_palindromic_substring(input):
    def check_palindrome(input):
        return "".join(input[::-1]).__eq__(input)
    length = len(input)
    pal = [input[i: j] for i in range(length) for j in range(i + 1, length + 1) if len(input[i: j])>1 and check_palindrome(input[i: j])]
    print(pal)
    print(max(pal, key=len))
    highest = pal[0]
    for str in pal:
        if len(str) > len(highest):
            highest = str
    return highest


# print(longest_palindromic_substring("ababaefg"))
# print(longest_palindromic_substring("forgeeksskeegfor"))
# print(longest_palindromic_substring("anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"))

############################################################################
students = [{'name': 'Alice', 'grade': 85},     {'name': 'Bob', 'grade': 90},     {'name': 'Charlie', 'grade': 80} ]
highest = 0
name = ""

for stu in students:
    if stu['grade'] > highest:
        highest = stu['grade']
        name = stu['name']

print(name)

List1 = [{'name': 'John', 'class': 12},[{"name": "Adam", "class": 5}]]
List1 = ([indiv for inner in List1 for indiv in (inner if isinstance(inner, list) else [inner])])

for lst in List1:
     kName = [k for k, v in lst.items() if v == lst['name']]
     kClass = [k for k, v in lst.items() if v == lst['class']]
     print(f"{kName[0]} is {lst['name']} and {kClass[0]} is {lst['class']}")
##############################################################################
# Write code to reverse vowel characters from a given string
inp = list("hello world")
vowe = "aeiouAEIOU"
vl = [v for v in inp if v in vowe]
print(vl)
for i,ch in enumerate(inp):
    if ch in vowe:
        inp[i] = vl.pop()

print("".join(inp))
################################################################################
l = ["h","e","l","l","o"]
for i in range(len(l)//2):
    tmp = l[i]
    l[i] = l[len(l)-1-i]
    l[len(l) - 1 - i] = tmp

print(l)
###############################################################################
s = "A man, a plan, a canal: Panama"
s = [c.lower() for c in s if c.isalnum()]
sp = "".join(s)
print(s)
print("".join(s[::5]))
###############################################################################
# Write code for longest common prefix
pre = ["reflower","flow","flight"]
# pre = ["flower","flower","flower","flower"]
pf = [p[0:i] for p in pre for i in range(1,len(p)+1)]
res=[]

for pfx in pf:
    count = 0
    for p in pre:
        if p.startswith(pfx):
            count +=1
        if count == len(pre):
            res.append(pfx)


print([] if len(res)<1 else max(res, key=len))
##############################################################################
# Wrirte code for longest substring w/o repeaing characters
s= "abcabcbbbabca"
used = {}
start = max_length = 0

for i, c in enumerate(s):
    if c in used and start <= used[c]:
        start = used[c] + 1
    else:
        max_length = max(max_length, i - start + 1)

    used[c] = i

print(max_length)
###############################################################################
# Write code to find sub array to find sum of target
ls = [1,2,3,4,5]
length = len(ls)
target = 3
right, left = 0,0
sub_arr = 0
res = 0
for right in range(length):
    sub_arr += ls[right]
    while sub_arr >= target:
        res = max(res, right - left + 1)
        sub_arr -= ls[left]
        left +=1

print(res)
###############################################################################
# write code to remove duplicate from list
dup_lst = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]
new_list = []
for item in dup_lst:
    if item not in new_list:
        new_list.append(item)

print(new_list)

###############################################################################
# Write code to rotate list for given times
inp = [1,2,3,4,5]
# o/p [4,5,1,2,3]
def rotate_list(lst, k):
    k %= len(lst)
    print(lst[-k:]+lst[:-k])
    for i in range(k):
        lst.insert(0,lst.pop())
    print(lst)

rotate_list(inp, 3)
###############################################################################
library_cate={'book1': {'title': 'The Great Gatsby', 'author': 'Harper Lee', 'year': 1925, 'genres': ['Fiction', 'Classics']},
              'book2': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'genres': ['Fiction', 'Classics']},
              'book3': {'title': "The Hitchhiker's Guide to the Galaxy", 'author': 'Douglas Adams', 'year': 1979, 'genres': ['Science Fiction', 'Comedy']}}

#Find the count of books that belong to the "Fiction" genre.

print([cate for cate in library_cate.values() if cate['genres'].__contains__("Fiction")])
cntr = 0
for cate in library_cate.values():
    if cate['genres'].__contains__("Fiction"):
        cntr += 1
print(cntr)

#Determine the list of unique authors in the library.
auth = {}
for cate in library_cate.values():
    if cate['author'] in auth:
        auth[cate['author']] += 1
    else:
        auth[cate['author']] = 1

print([k for k,v in auth.items() if v == 1])
#Create a new dictionary that groups books by their publication year.
grp_dict = {}
for title,metadata in library_cate.items():
    year = metadata['year']
    metadata.pop('year')
    grp_dict[year] = metadata
print(grp_dict)
#################################################################################
teams=['csk','rr','srh','pbks','rcb','mi']
results = [['w','w','n','n','n'],['w','l','n','n','n'],['w','w','w','n','n'],['w','l','n','n','n'],['l','l','n','n','n'],['l','w','n','n','n']]
# teams = "//div[@class='tb_c immersive-container tb_stc']//tr[@role='link']"
# results = f"//div[@class='tb_c immersive-container tb_stc']//tr[@role='link' and @aria-label='{name}']/td[@jsaction]/div[@class='YCyuEf']"
max_wins = 0
team_name = None
for team,result in zip(teams,results):
    consecutive_wins = 0
    for res in result:
        if res == "w":
            consecutive_wins += 1
        else:
            break

    if consecutive_wins > max_wins:
        max_wins = consecutive_wins
        team_name = team
print(team_name)
