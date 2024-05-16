import random
guess = 0
lister = [1,3,5,7,8,9]
def searcher(find_in:list,to_find:int,min_ind:int,max_ind:int):
    middex = (min_ind + max_ind)//2
    guess = find_in[middex]
    if guess == to_find:
        return middex
    if guess > to_find:
        max_ind = middex
    else:
        min_ind = middex  
    if max_ind <= min_ind+1:
        return max_ind
    return searcher(find_in,to_find,min_ind,max_ind)
if __name__ == '__main__':
    maxdex = len(lister)
    mindex = 0
    to_find = random.choice(lister)
    print(searcher(lister,to_find,mindex,maxdex))


