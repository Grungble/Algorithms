from bin_search_rec_p import searcher
import random
list_val_min = 0
list_val_max = 20
list_min= 0
list_max = 10
unsorted_list = []
sorted_list = []
def list_generator():
    for i in range(list_min,list_max):
        unsorted_list.append(random.randint(list_val_min, list_val_max))
    return unsorted_list
def sorter(s_list:list,u_list:list):
    mindex = 0
    maxdex = len(s_list)
    find_place = u_list.pop(0)
    if len(s_list) <1:
        s_list.append(find_place)
        return sorter(s_list,u_list)
    temp_placement = searcher(s_list,find_place,mindex,maxdex)
    if s_list[0] < find_place:
        s_list.insert(temp_placement,find_place)
    else:
        s_list.insert(temp_placement-1,find_place)
    if len(u_list) > 0:
        return sorter(s_list,u_list)
    else:
        return s_list
if __name__ == '__main__':
    print("sorted list",sorter(sorted_list, list_generator()))
    
        