# Calculate  hoe many times the list is rotated.

# 1)
# linear search
# Solution o(2n)
nums = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]


def count_rotation_lf(nums):
    mini = min(nums)
    for i in range(len(nums)):
        if nums[i] == mini:
            return i
    return -1


# print(count_rotationlf(nums))

# 2
# while loop
# solution o(n)


def count_rotation_lw(nums):
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position
        position += 1
    return 0


# print(count_rotation_lw(nums))


# 3)
# binary search
# Solution o(log(n))


def count_rotation_binary(nums):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]
        if mid_number < nums[mid-1]:
            return mid
        elif mid_number < nums[-1]:
            hi = mid-1
        else:
            lo = mid+1
    return -1


print(count_rotation_binary(nums))
