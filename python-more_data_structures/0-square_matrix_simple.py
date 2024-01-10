def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_i = [elem ** 2 for elem in i]
        new_matrix.append(new_i)
    return new_matrix
