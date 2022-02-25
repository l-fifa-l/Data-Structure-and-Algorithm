import numpy as np

twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [
                     9, 0, 10, 11], [12, 13, 14, 15]])
print(twoDArray)


def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])


accessElements(twoDArray, 2, 3)
