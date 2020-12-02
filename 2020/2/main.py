def handle(line):
    rules, test = line.strip().split(':')
    test = test.strip()

    bounds, target = rules.split()
    up, down = bounds.split('-')
    up = int(up)
    down = int(down)

    return (up, down, target, test)

def test1(item):
    up, down, target, test = item
    found = len(list(filter(lambda x: x == target, test)))
    return found >= up and found <= down

def test2(item):
    up, down, target, test = item
    up = up - 1
    down = down - 1
    return (test[up] == target) ^ (test[down] == target)

if __name__ == '__main__':
    with open('input') as file:
        rows = list(map(handle, file))
        print(len(list(filter(test1, rows))))
        print(len(list(filter(test2, rows))))
