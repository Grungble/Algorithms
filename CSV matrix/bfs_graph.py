

letter_dict = {'A': ['B','C', 'D'], 
               'B': ['C'], 
               'C': ['B'], 
               'D': [ 'C','E'], 
               'E': ['C','D']}


def queue_gen(node_dict:dict):
    do_not_go = set()
    my_queue = []
    #queues up the next place to go 
    if len(my_queue) == 0:
        for key,connections_list in node_dict.items():
            print(key)
            do_not_go.add(key)
            print('connecttions list', connections_list)
            for to_go in connections_list:
                my_queue.append(to_go)
                print('queue', my_queue)  
            break
    for go_to in my_queue:
        node_points_to = node_dict[go_to]
        if node_points_to in my_queue:
            pass
        else: 
            my_queue.append()
        do_not_go.add(go_to)
        


    return my_queue


if __name__ == '__main__':
    queue_gen(letter_dict)