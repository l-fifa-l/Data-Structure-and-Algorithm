from array import *

arr = array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def accessElement(array, index):
    if index > len(array):
        print('there is no element at this index')
    else:
        print(array[index])


accessElement(arr, 6)
