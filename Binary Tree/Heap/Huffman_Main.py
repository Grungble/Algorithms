import heapq
from string_counter import letter_counter
letter_dict = {}
str_to_encode = 'where did I go at the end of the day?'
# s_list = ['a','b','x','e','y','u','c','k']
# v_list = [12,  4,  16, 90, 21, 54, 8,  15]
    
class Node:
    def __init__(self,name:str,value:int):
        self.name = name
        self.value = value
        self.right = None
        self.left = None
    def __repr__(self):
        return f'Node(name={self.name},value={self.value})'
    def __lt__(self,other):
        #want the greatest val at the top 
        #need max heap ignore for right now
        return self.value < other.value
    
def huff(min_heap:heapq, node_list:list,Node_c:Node):
    if len(node_list) == 1:
        return node_list
    node1 = min_heap.heappop(node_list)
    node2 = min_heap.heappop(node_list)
    #print(node1)
    #print(node2)
    new_node = Node_c(node1.name + node2.name, node1.value + node2.value)
    new_node.left = node1
    new_node.right = node2
    #print(new_node)
    heapq.heappush(node_list, new_node)
    return huff(min_heap,node_list,Node_c)
if __name__ == '__main__':
    letter_counter(str_to_encode,letter_dict)
    print(letter_dict)
    # node_list = [Node(name,value) for name,value in zip(s_list,v_list)]
    node_list = [Node(name,value) for name,value in letter_dict.items()]
    heapq.heapify(node_list) #makes list heap
    print(node_list)
    print(huff(heapq, node_list, Node))
    
    
    