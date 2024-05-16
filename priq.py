class Kpq:
    def __init__ (self):#establishes list  
        self.pqueue = [] #self is the 
    def insert(self, new_value:int):#inserts values into the list
        self.pqueue.append(new_value)

    def delete(self,value_to_remove:int):
        self.pqueue.remove(value_to_remove)

    def peek(self):
        if len(self.pqueue) ==0:
            return None
        sorted_pq = sorted(self.pqueue)
        return sorted_pq[-1]
    def sorter(self):
        self.pqueue.sort
        return self.pqueue
    def dequeue(self):
        if len(self.pqueue) == 0:
            return None
        max_value = self.peek() #largest value is the highest priority
        self.pqueue.remove(max_value)
        return max_value
    def __len__(self):
        return len(self.pqueue)
    def __repr__(self):
        return f'priority queue list:{self.pqueue}'
    