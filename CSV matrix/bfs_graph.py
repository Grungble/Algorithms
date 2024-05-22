

letter_dict = {'A': ['B','C', 'D'], 
               'B': ['C'], 
               'C': ['B'], 
               'D': [ 'C','E'], 
               'E': ['C','D']}


def queue_gen(node_dict:dict):
    do_not_go = set()
    my_queue = []
    went_list = []
    #queues up the next place to go 
    if len(my_queue) == 0:
        for key,connections_list in node_dict.items():
            print(f'starting at{key}')
            do_not_go.add(key)
            went_list.append(key)
            print('connecttions list', connections_list)
            for to_go in connections_list:
                my_queue.append(to_go)
                print('queue', my_queue)  
            break
    for go_to in my_queue:
         pass


    print('where I went',went_list)
    return my_queue


if __name__ == '__main__':
    queue_gen(letter_dict)