import random
import math
max_range = 100
min_range = 0
lower_range = 0
guess = 0
unsorted_list = [3,5,8,1,7,9]
sorted_list = []
#generates then sorts an ordered list
# for i in range(lower_range, max_range):
#     unsorted_list.append(i)
#     random.shuffle(unsorted_list)

to_find = 20
#= random.choice(unsorted_list)
print("value to find",to_find)
#print(lister)
def bin_search(list:list, sorted:list):
    print("unsorted",list)
    value = list.pop(0)
    print("value whos place is being found",value)
    maxdex = len(list)
    mindex = 0
    max_tries = 1+ math.floor(math.log2(maxdex))
    counter = 0
    print("maxdex",maxdex)
    middex = (mindex + maxdex)//2
    guess = list[middex]
    if len(sorted)<1:
        sorted.append(value)
    print(f'{mindex} {middex} {maxdex}')
    print("sorted list",sorted)
    # if guess == value:
    #     return middex
    if guess > value:
        maxdex = middex
    else:
        mindex = middex
    counter +=1
    if maxdex <= mindex+1:
        print
        return(maxdex)
    else: 
        bin_search(list,sorted)
    if len(list)<1:
        print("about to return")
        return sorted
def sorter(ulist:list, slist:list,):
    max_in = len(ulist)
    min_in= 0

if __name__ == '__main__':
    print(bin_search(unsorted_list,sorted_list))

# while len(unsorted_list)>0:
#     variable = unsorted_list.pop(0)
#     print(unsorted_list)
#     if len(sorted_list) == 0:
#         sorted_list.append(variable)
#     print(sorted_list)
#     if len(sorted_list)>0:
#         sorted_list.insert(bin_search(sorted_list,variable),variable)
# sorted_list.append(unsorted_list.index(0))
# def iterative_sort():
#     maxer =
#     total_tries = 1+math.floor(math.log2(maxer))
#     while counter < total_tries
#         for i in (unsorted_list):
#             counter = 0 
#             sorted_list.append(unsorted_list.index(0))
        
# for i in (0, max_range):
#     guess = int((upper_range+lower_range)//2)
#     if guess == final_num:
#         print("W", guess)
#         break
#     elif guess > final_num:
#         lower_range = guess
#     elif guess < final_num:
#         upper_range = guess

#     print("upper",upper_range, guess,"lower",lower_range)

