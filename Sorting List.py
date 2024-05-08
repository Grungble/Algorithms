list  = [9,7,11,3,2,12,13]
sorted_list = []
iteration = 0
num = 0
previous = None
def check(list, val):
    for i in list:

     #sorted.append(i)
     if iteration < i:
        iteration = i
     if iteration == i: 
         for x in list:
             if val <= x:
                 print(x)
                 list.pop(x)