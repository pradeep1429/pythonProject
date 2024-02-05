pos = -1

def search(list, num):
    lBound = 0
    uBound = len(list) - 1
    mid = 0

    while lBound <= uBound:
        mid = (uBound + lBound) // 2

        if list[mid] == num:
            globals()['pos'] = mid
            return True
        elif list[mid] < num:
                lBound = mid + 1
        else:
                uBound = mid - 1
    return False

list = [2,4,9,12,23,67,99]



if search(list,67):
    print("found at pos {}".format(pos))
else:
    print("Not found")