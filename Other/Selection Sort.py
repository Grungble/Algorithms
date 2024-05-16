import time
unsorted_list  = [9,7,11,3,2,12,13]
sorted_list = []
iteration = 0
limiter = True
if len(unsorted_list) >20: #limits 
    limiter = False
while (limiter): 
    iteration = 0
    for x in unsorted_list:
        if iteration < x: #sets x as largest var in list
            iteration = x
    #if iteration >= all(unsorted_list): #failsafe, checks largest num
    sorted_list.insert(0,iteration)
    unsorted_list.remove(iteration)
    if len(unsorted_list) == 0: #once the unsorted list has no variables  it breaks the loop
        break
print("list sorted", sorted_list) #prints the sorted list