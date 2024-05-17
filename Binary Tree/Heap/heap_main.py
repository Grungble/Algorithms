from h_node import Node
heap = [7,5,6,10]
import random

def heapify(root:Node,listin:list,c_value:int):
    c_value += 1
    print(c_value)
    child_left = 2*c_value +1
    child_right = 2*c_value +2
    parent_right = (c_value+2)//2
    parent_left = (c_value+1)//2
    if child_left >= len(listin):
        return 'left too long'
    if child_right >= len(listin):
        return 'right too long'
    if listin[c_value] < listin[child_left]:
        #switch left child and parent
        listin[c_value],listin[child_left] = listin[child_left],listin[c_value] 
        print('variables switched left',listin)
        c_value -= 1
    if listin[c_value] < listin[child_right]:
        listin[c_value],listin[child_right] = listin[child_right],listin[c_value]
        print('variables switched right',listin)
        c_value -= 1
    if listin[c_value] > listin[parent_left]:
         listin[c_value],listin[parent_left] = listin[parent_left],listin[c_value]
    
    
    return heapify(root,listin,c_value)
# def __add__(root:Node,new_value:int,list_h:list):
#     if len(list_h) == 0:
#         root.value = new_value
#         list_h.append(new_value)
#         return list_h
#     if new_value > root.value:
#         root.value = new_value
#         list_h.insert(0,new_value)
#         print("replacing root with", new_value)
#         return list_h
#     else:
#         temp_place = list_h.index(root.value)
#     if list_h[(2(temp_place)+1)] < new_value:
#         list_h.insert(2(temp_place)+1,new_value)
#         print(list_h)




if __name__ == '__main__':
    for i in range(1,23):
        heap.append(i)
    random.shuffle(heap)
    my_heap = Node
    current_val = 0
    print(heapify(my_heap,heap,current_val))
