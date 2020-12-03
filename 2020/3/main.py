from functools import reduce

def traverse(x_step, y_step, rows):
    x_max = len(rows[0])
    x = 0
    y = 0

    count = 0
    while y < len(rows):
        if rows[y][x] == '#':
            count += 1

        y += y_step
        x = (x + x_step) % x_max

    return count

if __name__ == '__main__':
    with open('input') as file:
        rows = list(map(lambda x: x.strip(), file))
        print(traverse(3, 1, rows))
        print(reduce(lambda x, y: x * y, (
            traverse(1, 1, rows),
            traverse(3, 1, rows),
            traverse(5, 1, rows),
            traverse(7, 1, rows),
            traverse(1, 2, rows),
        )))
