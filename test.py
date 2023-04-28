import numpy as np
s = lambda x, y, i, j: -2 if x[i] != y[j] else 1
g = -2

def traceback(matrix, n, m,x,y):
    if m <= 0 or n <=  0:
        return

    matrix = matrix[:n+1,:m+1]
    print(matrix)

    align = matrix[n-1][m-1] + s(x, y, n-1, m-1)
    delete = matrix[n-1][m] + g
    insert = matrix[n][m-1] + g

    choise = max(align, delete, insert)
    if x[n-1] == y[m-1]:
        instructions.insert(0, "M")
        return traceback(matrix, n-1, m-1,x,y)
    else:
        if(choise == align):
            instructions.insert(0, "R")
            return traceback(matrix, n-1, m-1,x,y)
        elif(choise == delete):
            instructions.insert(0, "D")
            return traceback(matrix, n-1, m,x,y)
        else:
            instructions.insert(0, "I")
            return traceback(matrix, n, m-1,x,y)


def initialize_matrix(x, y):
    m, n = len(x), len(y)

    matrix = np.zeros((m+1, n+1))

    for i in range(1, m + 1):
        matrix[i][0] = i * g

    for j in range(1, n + 1):
        matrix[0][j] = j * g

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            align = matrix[i-1][j-1] + s(x, y, i-1, j-1)
            delete = matrix[i-1][j] + g
            insert = matrix[i][j-1] + g

            matrix[i][j] = max(align, delete, insert)

    traceback(matrix, len(x), len(y),x,y)
    return instructions

instructions = []
y='FMDTPLNE'
x='FKHMEDPLE'
'ATCGT'
'TGGTG'
instructions = initialize_matrix(x, y)
print(instructions)