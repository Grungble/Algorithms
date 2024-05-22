

from os.path import dirname, realpath
DIR=dirname(realpath(__file__))

def read_graph_file(fname:str):
    graph_dict = {}
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

if __name__ == '__main__':
    GRAPH_FNAME = 'graph_dict2.graph'
    my_graph_dict = read_graph_file(GRAPH_FNAME)
    print(my_graph_dict)
