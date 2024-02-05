
pos = -1

def search(list, num):
    i = 0
    while i<= len(list) - 1:
        if(list[i] == num):
            globals()['pos'] = i
            return True
        i += 1
    return False

list = [2,5,8,9,13,10]

if search(list,10):
    print("Found at pos {}".format(pos))
else:
    print("not found")