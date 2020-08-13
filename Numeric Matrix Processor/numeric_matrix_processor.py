```
import copy


def matrix():
    rows_a, columns_a = [int(x) for x in input('Enter size of first matrix:').split()]
    print('Enter matrix:')
    matrix = [[float(x) for x in input().split()] for row in range(rows_a)]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()


def add_matrices():
    matrix_a = matrix()
    matrix_b = matrix()

    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        matrix_added = [[(matrix_a[i][j] + matrix_b[i][j]) for j in range(len(matrix_a[0]))] for i in
                        range(len(matrix_a))]
        print_matrix(matrix_added)
    else:
        print("ERROR")


def multiply_by_constant(matrix_a, constant):
    matrix_mult = [[matrix_a[i][j] * constant for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    return matrix_mult


def multiply_matrices():
    matrix_a = matrix()
    matrix_b = matrix()

    result = [[0 for x in range(len(matrix_b[0]))] for x in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_a[0])):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    print_matrix(result)


def transose_diagonal(matrix_a):
    transose_matrix = [[matrix_a[j][i] for j in range(len(matrix_a))] for i in range(len(matrix_a[0]))]
    return transose_matrix


def side_diagonal():
    matrix_a = matrix()
    side_diagonal = [[matrix_a[len(matrix_a) - 1 - j][len(matrix_a[0]) - 1 - i] for j in range(len(matrix_a[0]))]
                     for i in range(len(matrix_a))]
    print('The result is:')
    print_matrix(side_diagonal)


def vertical_line():
    matrix_a = matrix()
    vertical_line = [[matrix_a[i][len(matrix_a[0]) - 1 - j] for j in range(len(matrix_a))]
                     for i in range(len(matrix_a[0]))]
    print('The result is:')
    print_matrix(vertical_line)


def horizontal_line():
    matrix_a = matrix()
    horizontal_line = [[matrix_a[len(matrix_a) - 1 - i][j] for j in range(len(matrix_a))]
                       for i in range(len(matrix_a[0]))]
    print('The result is:')
    print_matrix(horizontal_line)


def transose_matrix():
    us_input = input('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
    ''')
    if us_input == '1':
        matrix2 = matrix()
        matrix_tranc = transose_diagonal(matrix2)
        print('The result is:')
        print_matrix(matrix_tranc)
    elif us_input == '2':
        side_diagonal()
    elif us_input == '3':
        vertical_line()
    elif us_input == '4':
        horizontal_line()


def minor(matrix, i, j):
    new_matrix = copy.deepcopy(matrix)
    del new_matrix[i]
    for i in range(len(matrix[0]) - 1):
        del new_matrix[i][j]
    return new_matrix


def det(matrix):
    n = len(matrix[0])
    if n == 1:
        return matrix[0][0]
    signum = 1
    determinant = 0
    for j in range(n):
        determinant += matrix[0][j] * signum * det(minor(matrix, 0, j))
        signum *= -1
    return determinant


def matrix_cofactors(a):
    matrix_cofactors = [[0 for _ in range(len(a))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            matrix_cofactors[i][j] = det(minor(a, i, j)) * (-1) ** (i + j)
    return matrix_cofactors


def matrix_inverse():
    matrix1 = matrix()
    if det(matrix1) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        matrix_cof = matrix_cofactors(matrix1)
        matrix_cof_det = transose_diagonal(matrix_cof)
        matrix_inverse = multiply_by_constant(matrix_cof_det, (1 / det(matrix1)))
        print('The result is:')
        print_matrix(matrix_inverse)


while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    vari = input('Your choice:')
    if vari == '1':
        add_matrices()
    elif vari == '2':
        matrix_a = matrix()
        constant = int(input('Enter constant:'))
        print('The result is:')
        print_matrix(multiply_by_constant(matrix_a, constant))
    elif vari == '3':
        multiply_matrices()
    elif vari == '4':
        transose_matrix()
    elif vari == '5':
        mat = matrix()
        print('The result is:')
        print(det(mat))
    elif vari == '6':
        matrix_inverse()
    else:
        break
```
