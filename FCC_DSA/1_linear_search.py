cards = []
print(cards)
query = 1
print(query)


def lenear_search(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


print(lenear_search(cards, query))


# Edge cases
# 1. what if the query is the first element
# 2. what if the query is the last element
# 3. what is the query does not exist in the card
# 4. whatv if there are more cards of same number
