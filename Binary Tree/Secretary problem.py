import random
from matplotlib import pyplot
a_num = 10000
runtime = 10000
max_rank = 99
min_rank = 0
a_list =[]
h_list = 0
r = 0

def list_gen(applicants:list,num_app:int, rank_max:int,rank_min:int):
    applicants.clear()
    while len(applicants)-1 < num_app:
       applicants.append(random.randint(rank_min,rank_max))
    #print(applicants)
    return applicants 

def hire(applicants:list,list_length:int):
    global h_list
    global r
    # print(applicants)
    # print(applicants[0])
    for i in (applicants):
        if i > applicants[0]:
            if i == max(applicants):
                h_list += 1
                r +=i
                break
            else:
                break
    
if __name__ == '__main__':
    counter = 0
    while counter<runtime:
        list_gen(a_list,a_num,max_rank,min_rank)
        #print(a_list)
        hire(a_list,a_num)
        counter += 1
    print('runtime',runtime+1)
    print('applicants',a_num+1)
    print(h_list)
    print(f'{(h_list/(a_num*runtime))*100}%')
    print(r/(runtime+1))
    