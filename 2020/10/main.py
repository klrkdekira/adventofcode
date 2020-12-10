def part1(list):
    deltas = []
    prev = 0
    for i in list:
        deltas.append(i - prev)
        prev = i
    return deltas.count(1) * deltas.count(3)


def part2(list):
    d = {0: 1}
    for i in list[1:]:
        d[i] = d.get(i - 1, 0) + d.get(i - 2, 0) + d.get(i - 3, 0)
    return d[max(d.keys())]


if __name__ == '__main__':
    with open('input') as file:
        rows = sorted(map(int, file))
        rows = [0] + rows + [rows[-1] + 3]
        print(part1(rows))        
        print(part2(rows))
