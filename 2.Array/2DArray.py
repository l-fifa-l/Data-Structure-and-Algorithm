# Create 2D array
import numpy as np

twoDArray = np.array([[11, 15, 16], [19, 14, 77], [12, 13, 8]])
print(twoDArray)

# Insert in 2D Array
newTDArray = np.insert(twoDArray, 3, [[1, 2, 3]], 0)
print(newTDArray)
