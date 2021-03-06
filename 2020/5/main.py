from functools import reduce

def partition_row(p, q, cmd):
    d = int((q - p) / 2)
    if cmd == 'F':
        return (p, p + d)
    elif cmd == 'B':
        return (q - d, q)
    raise Exception(f'invalid cmd {cmd}')

def partition_col(p, q, cmd):
    d = int((q - p) / 2)
    if cmd == 'R':
        return (q - d, q)
    elif cmd == 'L':
        return (p, p + d)
    raise Exception(f'invalid cmd {cmd}')

def side(p, q, cmd):
    if cmd == 'F':
        return p
    elif cmd == 'B':
        return q
    if cmd == 'R':
        return q
    elif cmd == 'L':
        return p
    raise Exception(f'invalid cmd {cmd}')

def parse(s):
    row = (0, 127)
    col = (0, 7)
    x = 0
    y = 0
    for i, cmd in enumerate(s):
        if i < 6:
            p, q = row
            row = partition_row(p, q, cmd)
        elif i == 6:
            p, q = row
            y = side(p, q, cmd)
        elif i == 9:
            p, q = col
            x = side(p, q, cmd)
        else:
            p, q = col
            col = partition_col(p, q, cmd)

    return (y, x, y * 8 + x)

if __name__ == '__main__':
    with open('input') as file:
        rows = map(lambda x: x.strip(), file)
        seats = set(map(lambda x: x[2], map(parse, rows)))
        seat = max(seats)
        print(seat)

        real_seat_id = next(filter(lambda i: i not in seats and i + 1 in seats and i - 2 in seats, range(seat)))
        print(real_seat_id)
