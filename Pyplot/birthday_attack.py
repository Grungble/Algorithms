
import random 
import math 
from matplotlib import pyplot as plt
iters = 300
max_length = 2**16



for i in range(max_length):
    counter = 0
    i = 1000*i
    i += 10000
    for k in range(iters):
        birthday_set = set()
        for l in range(i+1):
            birthday_num = random.randint(0, 2**32)
            if birthday_num in birthday_set:
                counter +=1
                break
            else:
                birthday_set.add(birthday_num)
    if i%100 == 0:
        plt.plot(i,(counter//iters)*100)
        print(f'with {i} values you have a {(counter/iters)*100}% chance of overlap')
plt.show()
        

        

