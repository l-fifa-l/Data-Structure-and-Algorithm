arr = [1, 2, 3, 4, 5, 6, 7]
target = 6


def linear_search(arr, target):
    position = 0
    while target != arr[position]:
        position += 1
    return position


print(linear_search(arr, target))
