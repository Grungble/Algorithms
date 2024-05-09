import time
unsorted_list  = [9,7,11,3,2,12,13]
sorted_list = []
iteration = 0
num = 0
  
while True:
    iteration = 0
    for x in unsorted_list:
        if iteration < x:
            iteration = x
    if iteration >= all(unsorted_list): 
        sorted_list.insert(0,iteration)
        unsorted_list.remove(iteration)
    if len(unsorted_list) == 0:
        break
print("list sorted", sorted_list)