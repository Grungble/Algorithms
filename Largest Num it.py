import time 
list  = [9,7,11,3,2,12,13]
iteration = 0

for i in list:
     if iteration < i:
        iteration = i
if iteration >= all(list): 
   print("the largest number is", iteration)
   #time.sleep(2)