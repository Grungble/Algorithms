import random
import math
max_range = 99
min_range = 0
lower_range = 0
guess = 0
lister = [1,3,5,7,8,9]
list_size = 50
#generates then sorts an ordered list
# for i in range(lower_range, max_range):
#     lister.append(i)
#     lister.sort()
print("list length", len(lister))
to_find = random.choice(lister)
#to_find = random.choice(lister)
print("list",lister)
print("value to find",to_find)
#print(lister)
def bin_search(list, value):
    maxdex = len(list)
    mindex = 0
    max_tries = 1 + math.floor(math.log2(maxdex))
    counter = 0
    while counter < max_tries:
        middex = (mindex + maxdex)//2
        print(maxdex, middex, mindex)
        guess = list[middex]
        if guess == value:
            return middex
        if guess > value:
            maxdex = middex
        else:
            mindex = middex
        counter +=1
print(bin_search(lister,to_find))

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

