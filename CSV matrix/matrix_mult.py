#multiply and transform matricies

new_matrix = [
    [1,2,3],
    [3,4,2],
    [2,4,1]
]
new_vector = [2,3,4]
transposed_matrix = []

def matrix_trans(og_matrix:list):
    trans_matrix = []
    trans_matrix = og_matrix.copy()
    print(trans_matrix)
    for row in trans_matrix:
        for enum, val in enumerate(row):
            print(val)
        pass

def matrix_multi(matrix:list, vector:list):
    result_vector = []
    for row in matrix:
        temp_val = 0
        for m_val, v_val in zip(row, vector):
            temp_val = (m_val*v_val) + temp_val
            print(result_vector)
        result_vector.append(temp_val)
    print(result_vector)
    return result_vector



if __name__ == '__main__':
    matrix_multi(new_matrix, new_vector)