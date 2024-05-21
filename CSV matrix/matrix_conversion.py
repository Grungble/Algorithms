import csv
from os.path import dirname, realpath
DIR = dirname(realpath(__file__))

def read_graph_dict_csv( graph_csv_filename:str):

    new_graph_dict = {}
    
    with open (f'{DIR}/{graph_csv_filename}','rt') as inf:
        next(inf)
        csvreader = csv.reader(inf)
        for row in (csvreader):
            key = row[0]
            row_value_list = []
            for value in row[1:]:
                row_value_list.append(value)
            new_graph_dict[key] = row_value_list
    return new_graph_dict

def read_graph_adjmat_csv(graph_csv_filename:str):

    new_graph_list = []

    with open (f'{DIR}/{graph_csv_filename}', 'rt') as inf:
        next(inf)
        csvreader = csv.reader(inf)
        for row in csvreader:
            int_row = [eval(i) for i in row] 
            new_graph_list.append(int_row)
        # for list in new_graph_list:
        #     for en,i in list:
        #         temp = list.pop(en)

    return new_graph_list

if __name__ == '__main__':
    GRAPH_DICT_FNAME = 'graph_dict.csv'
    GRAPH_ADJMAT_FNAME = 'graph_adjmat.csv'

    print('\n ---- DICT')
    graph_dict = read_graph_dict_csv(GRAPH_DICT_FNAME)
    print(graph_dict)

    print('\n ---- ADJACENCY MATRIX')
    graph_adjmat_list = read_graph_adjmat_csv(GRAPH_ADJMAT_FNAME)
    print(graph_adjmat_list)
