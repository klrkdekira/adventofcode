def parse(item):
    item = item.strip()
    return (item[0], int(item[1:]))

bearings = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}

movement = {
    0: (0, 1),
    90: (1, 0),
    180: (0, -1),
    270: (-1, 0),
}

def part1(actions):
    bearing = bearings['E']
    x, y = 0, 0
    for action, n in actions:
        if action == 'L' or action == 'R':
            polarity = 1
            if action == 'L':
                polarity = -1
            bearing = (bearing + (n * polarity)) % 360
        else:
            dx, dy = 0, 0
            if action == 'F':
                dx, dy = movement[bearing]
            else:
                dx, dy = movement[bearings[action]]
            x += dx * n
            y += dy * n
    return abs(x) + abs(y)

rotation = {
    0: lambda x, y: (x, y),
    90: lambda x, y: (y, -x),
    180: lambda x, y: (-x, -y),
    270: lambda x, y: (-y, x),
    -90: lambda x, y: (-y, x),
    -180: lambda x, y: (-x, -y),
    -270: lambda x, y: (y, -x),
}

def part2(actions):
    bearing = bearings['N']
    wx, wy = 10, 1
    x, y = 0, 0
    for action, n in actions:
        if action == 'L' or action == 'R':
            polarity = 1
            if action == 'L':
                polarity = -1

            n = n % 360 * polarity
            fn = rotation[n]
            wx, wy = fn(wx, wy)
            bearing = (bearing + n) % 360
        elif action == 'F':
            dx = wx * n
            dy = wy * n
            x += dx
            y += dy
        else:
            dx, dy = movement[bearings[action]]
            wx += dx * n
            wy += dy * n 
    return abs(x) + abs(y)

if __name__ == '__main__':
    actions = []
    with open('input') as file:
        actions = list(map(parse, file))

    print(part1(actions))
    print(part2(actions))