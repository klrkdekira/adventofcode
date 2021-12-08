def parse(row):
    line = []
    for vents in row.strip().split('->'):
        x, y = vents.split(',')
        line.append((int(x), int(y)))
    return line


lines = []
with open('input') as file:
    lines = list(map(parse, file))


def debug(grid):
    for y in range(10):
        for x in range(10):
            c = '.'
            if (x, y) in grid:
                c = grid[(x, y)]

            if x == 9:
                print(c)
                continue
            print(c, end=' ')


def sign(n):
    if n < 0:
        return -1
    return 1


def diff(line, diag=False):
    a, b = line
    x0, y0 = a
    x1, y1 = b
    dx = x1 - x0
    dy = y1 - y0

    output = []
    if x0 == x1:
        s = sign(dy)
        for i in range(abs(dy)):
            output.append((x0, y0 + i * s))
        output.append(b)
    elif y0 == y1:
        s = sign(dx)
        for i in range(abs(dx)):
            output.append((x0 + i * s, y0))
        output.append(b)
    else:
        if diag:
            sx = sign(dx)
            sy = sign(dy)
            for i in range(abs(dx)):
                output.append((x0 + i * sx, y0 + i * sy))
            output.append(b)

    return output


def walk(map, line):
    for p in line:
        x, y = p
        if x >= 0 and y >= 0:
            if p in map:
                map[p] += 1
            else:
                map[p] = 1


map = {}

for line in lines:
    walk(map, diff(line))

print('part 1')
print(len(list(filter(lambda x: x > 1, map.values()))))

map = {}
for line in lines:
    walk(map, diff(line, True))

print('part 2')
print(len(list(filter(lambda x: x > 1, map.values()))))
