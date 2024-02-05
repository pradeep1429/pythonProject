import array as arr

a= arr.array("i",[4,45,56,3,4,6,4])
for i in range(0,len(a)):
    print(a[i], end=" ")

a.insert(0,5)
print("\r")
for i in range(0,len(a)):
    print(a[i], end=" ")

sa = a[2:5]
print("\r")
print(sa)
a.pop(2)
for i in range(0,len(a)):
    print(a[i], end=" ")
a.remove(4)
print("\r")
for i in a:
    print(i, end=" ")
