import numpy as np

#get the max value of a 2d array
matrix = np.array([[10,50,30],[60,200,40],[100,150,2]])
row, column = np.unravel_index(matrix.argmax(), matrix.shape)
print(f'The max number is at index {row, column} and it is {matrix[row][column]}')