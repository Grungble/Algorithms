import math
import time
a=0
male1 = [2,1,3]
male2 = [1,3,2]
male3 = [3,2,1]
female1 = [1,3,2]
female2 = [1, 2, 3]
female3 = [3,2,1]
males = [male1, male2, male3]
females = [female1, female2, female3]
m_num = 0
f_num = 0
# print(female1.index(1))
# if male1.index(1)==0 & female1.index(1)==0:
#     print("Match Found!")
#     print("Male1 and Female1 are Compatible!")
while (len(females))>0:
    for male_it, m1 in enumerate(males):
        time.sleep(.75) 
        for female_it, f1  in enumerate(females):
            if m1.index(1) == f1.index(1):
                print("Pair Found", "Male",male_it+1+m_num, m1, "female",female_it+1+f_num, f1)
                f_num +=1
                females.remove(f1)
                break
            
    if(len(females))> 0:
        break        
print("done")