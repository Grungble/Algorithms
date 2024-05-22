
letter_dict = {'A': ['B', 'F', 'J'], 
               'B': ['A', 'E', 'C'], 
               'C': ['B', 'E', 'D'], 
               'D': ['C'], 
               'E': ['B', 'C'], 
               'F': ['A', 'G'], 
               'G': ['F', 'H', 'I'], 
               'H': ['G', 'I'], 
               'I': ['G', 'H'], 
               'J': ['A', 'K'], 
               'K': ['J']}
# {'A': ['B','C','D'], 
#                'B': ['C'], 
#                'C': ['B'], 
#                'D': ['C','E'], 
#                'E': ['C','D']}
matrix_list = []

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

if __name__ == '__main__':
    print(converter(letter_dict,matrix_list))

