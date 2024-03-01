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