import numpy as np

#get the max value of a 2d array
def getMax(matrix):

    row, column = np.unravel_index(matrix.argmax(), matrix.shape)
    print(f'The max number is at index {row, column} and it is {matrix[row][column]}')
    return row,column