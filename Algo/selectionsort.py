

def sort(list):
    length = len(list)
    for i in range(length-1):
        minPos = i
        for j in range(i,length):
           if(list[j] < list[minPos]):
               minPos = j

        temp = list[i]
        list[i] = list[minPos]
        list[minPos] = temp
        print(list)

list = [15,23,8,76,37,2]


sort(list)

