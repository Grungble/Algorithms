import time 
list  = [9,7,11,3,2,12,13]
sorted_list = []
iteration = 0

for i in list:

     #sorted.append(i)
     if iteration < i:
        iteration = i
     if iteration == i: 
         print(i)
         time.sleep(2)