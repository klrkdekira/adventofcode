def to_range(s):
    a, b = s.split("-")
    a, b = int(a), int(b)
    return lambda x: x >= a and x <= b


def parse_rule(line):
    key, values = line.split(":")
    rules = list(map(to_range, values.split("or")))
    return (
        key.strip(),
        lambda foo: any(map(lambda rule: rule(foo), rules)),
    )


def parse_ticket(line):
    return list(map(lambda x: int(x), line.split(",")))


def parse(lines):
    rules = []
    tickets = []
    nearby = []

    i = 0
    for line in lines:
        if not line:
            i += 1
            continue

        if line.startswith("your ticket"):
            continue
        elif line.startswith("nearby tickets"):
            continue

        if i == 0:
            rules.append(parse_rule(line))
        elif i == 1:
            tickets.extend(parse_ticket(line))
        elif i == 2:
            nearby.append(parse_ticket(line))
        else:
            raise Exception("what is this range?", i)
    return (dict(rules), tickets, nearby)


def separate(rules, nearby):
    invalids, valids = [], []
    for row in nearby:
        count = 0
        for j in row:
            found = any(map(lambda rule: rule(j), rules.values()))
            if not found:
                invalids.append(j)
                continue
            count += 1
        if count == len(row):
            valids.append(row)
    return invalids, valids


def part2(rules, tickets, nearby):
    discards, seats = {}, {}
    for row in nearby:
        for (i, seat) in enumerate(row):
            if not seats.get(i):
                seats[i] = []
                discards[i] = []

            for (name, rule) in rules.items():
                if rule(seat):
                    if name not in seats[i] and name not in discards[i]:
                        seats[i].append(name)
                else:
                    if name in seats[i]:
                        seats[i].remove(name)
                    discards[i].append(name)

    seats = seats.items()
    results = []

    while len(seats) > 0:
        seats = list(
            reversed(sorted(seats, key=(lambda seat: (len(seat[1]), seat[0]))))
        )

        id, name = seats.pop()
        name = name[0]
        results.append((name, id))

        for (i, seat) in enumerate(seats):
            _, v = seat
            if name in v:
                seats[i][1].remove(name)

    count = 1
    for name, i in results:
        if name.startswith("departure"):
            count *= tickets[i]
    return count


if __name__ == "__main__":
    lines = []
    with open("input") as file:
        lines = list(map(lambda x: x.strip(), file))

    rules, tickets, nearby = parse(lines)
    invalids, valids = separate(rules, nearby)
    print(sum(invalids))
    print(part2(rules, tickets, valids))
