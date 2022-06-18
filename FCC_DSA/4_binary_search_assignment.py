"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
"""

arr = [4, 5, 6, 9, 0, 2, 3]


def min_num_rotation(arr):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        print("Mid value Of list is", mid)
        if arr[mid - 1] > arr[mid]:
            return mid
        elif arr[mid] < arr[-1]:
            hi = mid-1
        elif arr[mid] > arr[-1]:
            lo = mid+1

    return -1


# print("Number of rotations are", min_num_rotation(arr))

'''
So far the assumed that the numbers in the list are unique. What if the numbers can repeat? E.g. [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]. modify the solution to handle this special case?
'''


arr = [2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 9, 9, 9, 2, 2, 2]


def min_num_rotation_repeat(arr):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        print("Mid value Of list is", mid)
        if arr[mid - 1] > arr[mid]:
            return mid
        elif arr[mid] < arr[-1]:
            hi = mid-1
        elif arr[mid] > arr[-1]:
            lo = mid+1
    return -1


# print(min_num_rotation_repeat(arr))


"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.

Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.

HINT: One way to solve this problem is to identify two sorted subarrays within the given array (using the count_rotations_binary function defined above), then perform a binary search on each subarray to determine the position of the target element. Another way is to modify count_rotations_binary to solve the problem directly.
"""

arr = [5, 6, 9, 0, 2, 3, 4]
target = 0


def mid_in_rotated_list(arr):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid-1] > arr[mid]:
            return mid
        elif arr[mid] < arr[-1]:
            hi = mid-1
        else:
            lo = mid-1


def locate_target(arr, target):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid+1
        else:
            hi = mid-1


def search_in_rotated_list(arr, target):
    partition = mid_in_rotated_list(arr)
    print("Partition is", partition)
    arrmore = arr[:partition]
    arrless = arr[partition:]
    if partition in arrless:
        return locate_target(arrless, target)
    else:
        return locate_target(arrmore, target)


# print(search_in_rotated_list(arr, target))

def locate_in_rotated_list(arr, target):
    mid = mid_in_rotated_list(arr)
    if target in arr[:mid]:
        return locate_target(arr, target)
    elif target in arr[mid:]:
        return locate_target(arr[mid:], target)+len(arr[:mid])

    return -1


print(locate_in_rotated_list(arr, target))
