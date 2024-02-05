#Reference Counting: Python primarily uses reference counting as its garbage collection technique.
# Each object in Python maintains a count of the number of references to it.
# Whenever the number of references to an object drops to zero, the memory occupied by the object is cleaned up automatically.
import sys

x = 10    # create an object
y = x     # increase the reference count
print(sys.getrefcount(x), sys.getrefcount(y))
print(id(x), id(y))
del x     # decrease reference count
# del y     # by deleting y, the count hits zero and the object is cleaned up
print(sys.getrefcount(y))

a = 43
b=a
print(sys.getrefcount(a), sys.getrefcount(b))

a="sdf"
print(id(a), id(b))
print(sys.getrefcount(a), sys.getrefcount(b))

#Cycle Detection: Reference counting is simple and effective but it doesn't account for reference cycles -
# where objects reference each other, creating a cycle and therefore it can not be deallocated.
# Python's garbage collector also uses a cyclic garbage collector, which can detect and clean up these cycles.

#global interpreter lock

def func(l=[]):
    l.append(2)
    print(l)

func([1])
func()