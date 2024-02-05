def bubblesort(list):


   for iter_num in range(len(list)-1,0,-1):
      for i in range(iter_num):
         if list[i]>list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
      print(list)
               
               
list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)