#multiply and transform matricies

new_matrix = [[0, 1.0, 0.5, 0.25, 1.0], 
              [0.5, 0, 0.5, 0.25, 0], 
              [0.5, 0, 0, 0.25, 0], 
              [0, 0, 0, 0, 0], 
              [0, 0, 0, 0.25, 0]]


new_vector = [2.75,1.25,.75,0,.25]
transposed_matrix = []

def matrix_trans_ALT(in_matrix:list):
    tran_p_matrix = list(zip(*in_matrix))
    return tran_p_matrix

def matrix_trans(og_matrix:list):
    trans_matrix = []
    for i in range(len(og_matrix)):
        new_row = [0 for i in range(len(og_matrix))]
        # print(new_row)
        # print(i)
        for enum, row in enumerate(og_matrix):
            new_val = row.pop(0)
            new_row[enum] = new_val
        trans_matrix.append(new_row)
        #print(trans_matrix)        
    return(trans_matrix)
def matrix_multi(matrix:list, vector:list):
    result_vector = []
    for row in matrix:
        temp_val = 0
        for m_val, v_val in zip(row, vector):
            temp_val = (m_val*v_val) + temp_val
            #print(result_vector)
        result_vector.append(temp_val)
    # print(result_vector)
    return result_vector



if __name__ == '__main__':
    #matrix_multi(new_matrix, new_vector)
    print(new_matrix)
    transposed_matrix = matrix_trans_ALT(new_matrix)
    print(transposed_matrix)
    