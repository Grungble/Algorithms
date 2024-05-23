import csv
from os.path import dirname, realpath
from matrix_mult import matrix_multi, matrix_trans
from matplotlib import pyplot as plt
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
                adj_list.sort()
                graph_dict[key_node] = adj_list
    return graph_dict

def converter(graph_dict:dict,matrix:list):
    key_list = []
    for key in graph_dict:
        key_list.append(key)
    key_list.sort()
    print('key_list',key_list)
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

def voting(vote_matrix:list):
    vote_value_list = []
    #assumes order
    for vote_val in (vote_matrix):
        value = 1/sum(vote_val)
        vote_value_list.append(value)
    for power , voter in zip(vote_value_list, vote_matrix):
        for enum,i in enumerate(voter):
            if i == 1:
                voter[enum] = power  
    print(graph_matrix)
    trnf_matrix = matrix_trans(vote_matrix)
    return trnf_matrix

def calc_vote(matrix, vector,counter,limit,point):
    points = []
    while counter <= limit:
        vector = matrix_multi(matrix,vector)
        points.append(vector[point])
        counter +=1
    return points

if __name__ == '__main__':
    VOTE_RANK_GRAPH = 'vote_rank.csv'
    counter = 0
    track = 1
    max_lim = 1000
    x_lim = [i for i in range(max_lim+1)]
    plt.ylim(0,3)
    read_graph_file(VOTE_RANK_GRAPH, graph_dict)
    print(graph_dict)
    converter(graph_dict,graph_matrix)
    print(graph_matrix)
    trasn_matrix = voting(graph_matrix)
    reputation = [1 for num in  range(len(trasn_matrix[0]))]
    calc_vote(trasn_matrix,reputation,counter, max_lim, track)
    for i in range(5):
        plt.plot(x_lim,calc_vote(trasn_matrix,reputation,counter, max_lim, i))
    plt.show()
   