def add_value(arr):
    result = 0
    for val in arr:
        result += val
    return result

def average_value(arr):
    total = 0
    for val in arr:
        total += val
    return total / len(arr)

print(add_value([1,2,3,4]))
print(average_value([1,2,3,4]))
# summing operation is written twice here - violation

def add_values(arr):
    return sum(arr)

def average_values(arr):
    return add_values(arr) / len(arr)

print(add_values([1,2,3,4]))
print(average_values([1,2,3,4]))