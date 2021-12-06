seq = []
cards = []

with open("input") as file:
    seq = next(file).split(",")

    card = []
    for row in file:
        row = row.strip()
        if not row:
            if card:
                cards.append(card)
            card = []
            continue
        card.append(row.split())
    cards.append(card)

# help to debug
def pprint(card):
    for row in card:
        print("{0: >2} {1: >2} {2: >2} {3: >2} {4: >2}".format(*row))
    print()


def win_yet(card):
    for row in card:
        if all(map(lambda x: x == "x", row)):
            return sum_of_unmarked(card)

    n = len(card)
    for p in range(n):
        count = 0
        for q in range(n):
            if card[q][p] == "x":
                count += 1
        if count == n:
            return sum_of_unmarked(card)

    return None


def move(card, n):
    for p, row in enumerate(card):
        for q, col in enumerate(row):
            if col == n:
                card[p][q] = "x"


def sum_of_unmarked(card):
    total = 0
    for row in card:
        for i in row:
            if i != "x":
                total += int(i)
    return total


def part_1(seq, cards):
    for i in seq:
        for card in cards:
            move(card, i)

            winning = win_yet(card)
            if winning:
                return int(i) * winning


def part_2(seq, cards):
    boards = {i: 0 for i in range(len(cards))}
    for i in seq:
        for board, card in enumerate(cards):
            move(card, i)

            winning = win_yet(card)
            if winning:
                boards[board] = 1
                if sum(boards.values()) == len(cards):
                    return int(i) * winning


print("part 1")
print(part_1(seq, cards))
print("part 2")
print(part_2(seq, cards))
