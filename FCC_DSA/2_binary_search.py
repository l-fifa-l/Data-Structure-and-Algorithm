cards = [13, 11, 10, 8, 7, 6, 5, 4, 3, 2, 1]
query = 7


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print('mid:', mid, 'mid_number:', mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    low, high = 0, len(cards)-1

    while low <= high:
        mid = (low+high)//2
        result = test_location(cards, query, mid)
        mid_number = cards[mid]
        print('low:', low, 'high:', high, 'mid:',
              mid, 'mid_number:', mid_number)
        if result == 'found':
            return mid
        elif result < 'left':
            high = mid-1
        elif result > 'right':
            low = mid+1
    return -1


print(locate_card(cards, query))
