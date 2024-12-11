def sparse_matrix_multiplication(matrix_a, matrix_b):

    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    
    sparse_a = get_dict_of_nonzero_cells(matrix_a)
    sparse_b = get_dict_of_nonzero_cells(matrix_b)

    # print(sparse_a)
    # print(sparse_b)

    matrix_c = [[0]*len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i, k in sparse_a.keys():
        # print(i, k)
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i,k)]*sparse_b[(k, j)]

    return matrix_c
def get_dict_of_nonzero_cells(matrix):
    dict_of_nonzero_cells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dict_of_nonzero_cells[(i,j)] = matrix[i][j]
    return dict_of_nonzero_cells

if __name__=="__main__":
    matrix_a = [
        [46, 0, 0],
        [45, 47, 0],
        [0, 0, 0],
        [34, 0, 25],
        [0, 2, 0],
        [0, 0, 0],
    ]
    matrix_b = [
        [26, 34, 20, 31, 34, 15],
        [38, 30, 23, 1, 45, 22],
        [47, 9, 9, 5, 9, 31],
    ]

    sol = sparse_matrix_multiplication(matrix_a, matrix_b)
    print(sol)