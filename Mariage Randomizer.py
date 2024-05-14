import time
import math
import random

Num_people = 5
Wives_list = []
husbands_list = []
husband_diction = {} #each wive's husband rankings
Wife_Diction = {}
match_diction = {}
temp_dic = {}
h_rank = 0
w_rank = 0
for i in range(Num_people):#generates the lists to be shuffled
    Wives_list.append(f'w{i+1}')
    husbands_list.append(f'h{i+1}')
for en, i in enumerate(range(Num_people)): 
    Wives_ranking = Wives_list.copy()
    husbands_ranking = husbands_list.copy()
    random.shuffle(Wives_ranking)
    random.shuffle(husbands_ranking)
    Wife_Diction.update({f'h{en+1}' :Wives_ranking}) #add husbands ranking of wives to dictionary
    husband_diction.update({f'w{en+1}':husbands_ranking})#add wives ranking of husband to dictionary
#pair people together
#itterates wives list and husband rankings
def w_cheat_checker(p_cheater,checked,rankings,gender_list,checked_p):
            #c_part is the current partner
            #p_cheater is who is currently being checked against the first partner
            #check_a is who is getting checked against
            c_part = match_diction.get(p_cheater)
            list_1 = gender_list.get(p_cheater)
            nil = list_1.index(c_part)
            for i in nil:
                if rankings.index(c_part)> c_part: 
                    print("hello")


for h_key, h_value in (husband_diction.items()):
    if not h_key in match_diction.keys():
        for w_key,w_value in (Wife_Diction.items()):
            if not w_key in match_diction.values():
                match_diction.update({h_key:w_key})
        # del (h_key, w_key)
for wife, husband in (match_diction.items()):#grabs pair 
    #wife is key:husband is value
    temp_h = husband_diction.get(wife)#grabs rankings of husbands
    temp_w = Wife_Diction.get(husband)#grabs rankings of wifes
    #print(temp_w)
    if temp_h.index(husband)> 0: #checks wife ranks husband bellow #0
        h_rank = temp_h.index(husband)#what husband is ranked
        
            
            
        for en,i in enumerate(temp_h):#checks who is ranked higher than husband
            #i is the husband currently being checked
            if en>= h_rank:#prevents iterations beyond current husband
                print("hello")
                break
            # if w_cheat_checker() == True:
            #     print("hello")
    print(wife,"ranks",husband,temp_h.index(husband))
    if temp_h.index(husband) <1: #check husband rank
        print(wife, "will not cheat on", husband)
    if temp_w.index(wife) < 1:
         print(husband, "will not cheat on",wife)
    if temp_h.index(husband) <1 & temp_w.index(wife) < 1:
        print(temp_h,"and",temp_w,"are stable") 
    