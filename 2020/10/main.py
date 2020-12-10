def part1(list):
    deltas = []
    prev = 0
    for i in list:
        deltas.append(i - prev)
        prev = i
    return deltas.count(1) * deltas.count(3)


def part2(list):
    d = {}
    for i, item in enumerate(list):
        d[item] = []
        for j in list[i+1:i+4]:
            if j - item <= 3:
                d[item].append(j)       

    x = {list[-1]: 1}
    for i in reversed(list[:-1]):
        count = 0
        for j in d[i]:
            count += x[j]
        x[i] = count
    return x[0]


if __name__ == '__main__':
    with open('test') as file:
        rows = sorted(map(int, file))
        rows = [0] + rows + [rows[-1] + 3]
        print(part1(rows))        
        print(part2(rows))
