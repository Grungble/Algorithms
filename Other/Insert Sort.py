unsorted_list  = [9,7,11,3,2,12,13]
sorted_list = []
value = 0 #value taken from unsorted list
position = 0 #the current position in sorted list
slen=len(sorted_list) #length of the sorted list
def insert_sorter(sorted_list:list,unsorted_list:list):
    temp_add = unsorted_list.pop(0)
    print('temp add', temp_add)
    if len(sorted_list) <1 :
            sorted_list.append(temp_add)
            print('first try', sorted_list)
            return insert_sorter(sorted_list, unsorted_list)
    for enum, i in enumerate(sorted_list):
        if temp_add > i:
            sorted_list.insert(enum+1, temp_add)
            print(sorted_list)
            break
    if len(unsorted_list) < 1:
        return 'done'
    return insert_sorter(sorted_list, unsorted_list)

if __name__ == '__main__':
    print(len(sorted_list))
    print(insert_sorter(sorted_list, unsorted_list))
