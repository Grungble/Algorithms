from bin_search_rec import searcher
import random
list_min = 0
list_max = 20
mindex = 0
maxdex = 10
unsorted_list = []
sorted_list = []
#generates random variables in the list
def list_generator():
    for i in range(mindex,maxdex):
        unsorted_list.append(random.randint(list_min, list_max))
    return unsorted_list
def sorter(s_list:list,u_list:list):
    mindex = 0
    maxdex = len(s_list)
    #print(u_list)
    find_place = u_list.pop(0)
    if len(s_list) <1:
        s_list.append(find_place)
        #print("value added", s_list)
        return sorter(s_list,u_list)
    if len(s_list) >= 0:
        temp_placement = searcher(s_list,find_place,mindex,maxdex)
        #print("temp", temp_placement)
        if s_list[0] < find_place:
            s_list.insert(temp_placement,find_place)
        else:
            s_list.insert(temp_placement-1,find_place)
        #print("sorted list",s_list)
        if len(u_list) > 0:
            return sorter(s_list,u_list)
        else:
            return s_list
    #searcher(find_in:list,to_find:int,min_ind:int,max_ind:int)
    
    
if __name__ == '__main__':
    print("sorted list",sorter(sorted_list, list_generator()))
    
        