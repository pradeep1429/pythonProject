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


get_count("AACABBCDDAD")
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
    print(k,v)
    if k.__eq__("city"):
        dic.update({k:swap_case(v, "camel")})
    else:
        dic.update({k: swap_case(v, "swap")})
    print(dic)

##############################################################################
# Write python code for li1 = [1,2,3,4,4,4,5,8] li2=[2,2,3,6,7]
# print common elements from both elements do not use sets.
li1 = [1,2,3,4,4,4,5,8]
li2=[2,2,3,6,7]
res = []
for i in li1:
    for j in li2:
        if i == j:
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
        res += d ** 3
    return res.__eq__(n)

print(check_armstrong(153))
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