import time
unsorted_list  = [9,7,11,3,2,12,13]
sorted_list = []
iteration = 0
num = 0
  
while True:
    iteration = 0
    for x in unsorted_list:
        print(x)
    #sorted.append(i)
        if iteration < x:
            iteration = x
    if iteration >= all(unsorted_list): 
        print(iteration)
        sorted_list.insert(0,iteration)
        unsorted_list.remove(iteration)
        print(sorted_list)
        print(unsorted_list)
    time.sleep(1)
    if len(unsorted_list) == 0:
        break
    #sorted_list.append(iteration)
    #list.remove(i)
    # print(sorted_list)
print("list sorted", sorted_list)