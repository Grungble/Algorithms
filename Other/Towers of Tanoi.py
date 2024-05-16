import random
import math
origional_stack = [2,1]
to_stack = []
hold_stack = []
length_stack = len(origional_stack)
class ring:
    def __init__(self,name:str, value:int):
        self.name = name
        self.value = value

def hanoi(num_discs:int,frm_s:list,to_s:list,hld_s:list):
    counter = 0 
    counter = counter + 1
    
    #solve for one
    if len(frm_s) == num_discs:
        to_s.append(origional_stack.pop())
        print(to_s)
    #solve for all others
    
    hanoi(num_discs,frm_s,to_s,hld_s)
        
if __name__ == '__main__':
    print(hanoi(length_stack,origional_stack,to_stack,hold_stack))