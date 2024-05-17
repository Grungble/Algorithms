import random
a_num = 500
runtime = 10000
max_rank = 99
min_rank = 0
a_list =[]
h_list = 0

def list_gen(applicants:list,num_app:int, rank_max:int,rank_min:int):
    applicants.clear()
    while len(applicants)-1 < num_app:
       applicants.append(random.randint(rank_min,rank_max))
    #print(applicants)
    return applicants 

def hire(applicants:list,list_length:int):
    global h_list
    # print(applicants)
    # print(applicants[0])
    for i in (applicants):
        if i > applicants[0]:
            if i == max(applicants):
                h_list += 1
            else:
                break
    
if __name__ == '__main__':
    
    for i in range(10):
        h_list = 0
        counter = 0
        while counter<runtime:
            list_gen(a_list,a_num,max_rank,min_rank)
            #print(a_list)
            hire(a_list,a_num)
            counter += 1
        print(h_list)
    