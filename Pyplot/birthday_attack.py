
import random 
from matplotlib import pyplot as plt
iters = 10000
max_length = 2**160
iteration_list  = []
overlap_pct = []


for i in range(max_length):
    counter = 0
    i = 100*i
    #i += 10000
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
        iteration_list.append(i)
        overlap_pct.append((counter/iters)*100)
        print(f'with {i} values you have a {(counter/iters)*100}% chance of overlap')
        if (counter//iters)*100 == 100:
            break
print(f'iterations:{iteration_list}')
print()
print(f'overlap: {overlap_pct}')
plt.plot(iteration_list,overlap_pct)
plt.show()