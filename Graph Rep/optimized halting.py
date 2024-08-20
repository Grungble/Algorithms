import random 
import math
from matplotlib import pyplot as plt 
 

p_num = 1000
r_range = 100
r_list = []
canidate_list = []
def generator(num_people = int, rank_range = int):
    rank_list = []
    for i in range(num_people):
        temp_rank = random.randint(0,rank_range)
        rank_list.append(temp_rank)
    return rank_list
def optimizer(applicant_list = list, checkpoint = int):
    global r_list

    largest_num = 0
    for p in range(checkpoint):
        if len(applicant_list) == 1:
            print(f'only applicant left {applicant_list}')
            return
        check_num = applicant_list.pop(0)
        if check_num > largest_num:
            largest_num = check_num
    print(f'largest number = {largest_num}')
    for enum, i in enumerate(applicant_list):
        if i > largest_num: 
            print(f'applicant found: applicant number:{enum}, rank:{i}')
            r_list.insert(i,0)
            applicant_list.insert(checkpoint,0)
            return 
        

    return


def n_optimizer( applicant_list = list, r = int):
    largest_num = 0
    global r_list
    global canidate_list
    #finds the largest number within the first r variables
    #in the list
    for i in range(r):
        x = applicant_list[i]
        if x > largest_num:
            largest_num = x
            #print(f'new largest number:{largest_num}')
    for enum, v in enumerate(applicant_list):
        #skips the r period
        if enum <= r:
            pass
        else:
            if v >= largest_num:
                if r >= enum:
                    print('error')
                    return 'error'
                print(f'r:{r}, largest num:{largest_num}, canidate placement:{enum}, canidate rank:{v}')
                r_list.insert(0,r)
                canidate_list.insert(0,v)
                return v


if __name__ == '__main__' :
    
    # #print(rank_list)
    # for i in range(100): 
    #     for r in range(10):
    #         rank_list = generator(p_num,r_range)
    #         optimizer(rank_list,i)
    
    # print(r_list)
   
    # n_optimizer(rank_list, 5)
    # print(rank_list)
    #range of r
    for r in range(101):
        #iterations
        for i in range(1000):
            rank_list = generator(p_num,r_range)
            x = n_optimizer(rank_list, r)
            # print(x)
    print(canidate_list)
    print(r_list)
    plt.plot( r_list, canidate_list, color='green')
    plt.show()

