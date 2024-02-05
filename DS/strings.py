
strr = "i am learning python"

print(strr.count("i",0,len(strr)))
print(strr[5], " ", strr[-9])
print(strr.capitalize())
print("".join(reversed(strr)))
print(strr.split(" "))
print(strr.islower(), strr.isalpha())
str1 = ("i am "
        "learning \n"
        "python")
print(str1)
# print(dir(int))
print(dir(str))

class GeeksforGeeks(object):
    def __str__(self):
         return "GeeksforGeeks"
    # def __repr__(self):
    #      return "testks"




print(repr(GeeksforGeeks())) # prints obect
print(GeeksforGeeks()) # prints GeeksforGeeks

