import csv
from os.path import dirname, realpath
DIR = dirname(realpath(__file__))
graph_dict = {}
graph_matrix = []
def read_graph_file(fname:str,graph_dict:dict):
    
    ifname = f'{DIR}/{fname}'
    with open(ifname, 'rt') as inf:
        for row in inf:
            if row[0] == '#':
                pass
            else:
                left_str, right_str = row.split(':')
                key_node = left_str.strip()

                adj_list = []
                for ch in right_str.strip():
                    adj_list.append(ch)
                graph_dict[key_node] = adj_list
    return graph_dict

def converter(graph_dict:dict,matrix:list):
    key_list = []
    for key in graph_dict:
        key_list.append(key)
    key_list.sort()
    for key in (graph_dict):
        connections = graph_dict.get(key)
        new_row = []
        connections.sort()
        for i in (key_list):
            if i in connections:
                new_row.append(1)
            else:
                new_row.append(0)
            #print('key and new row',key,new_row)
        matrix.append(new_row)
    return matrix
def voting(vote_matrix:list,voter_dict:dict):
    voter_list = []
    vote_value_list = []
    initial_vote_val = 1
    #assumes order
    for key in voter_dict:
        voter_list.append(key)
    for vote_val in (vote_matrix):
        value = 1/sum(vote_val)
        vote_value_list.append(value)
    print(vote_value_list)
    #take the vote val and 
    for i in zip():
        pass
    
if __name__ == '__main__':
    VOTE_RANK_GRAPH = 'vote_rank.csv'
    read_graph_file(VOTE_RANK_GRAPH, graph_dict)
    print(graph_dict)
    converter(graph_dict,graph_matrix)
    print(graph_matrix)
    voting(graph_matrix,graph_dict)