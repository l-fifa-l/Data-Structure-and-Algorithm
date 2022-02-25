from array import *

arr = array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "the element does not exist in this array"


print(searchInArray(arr, 45))
