def to_grid(seats):
    d = {}
    for y, row in enumerate(seats):
        d[y] = {}
        for x, seat in enumerate(row):
            d[y][x] = seat
    return d

def count_occupied(seats):
    count = 0
    for y, row in seats.items():
        for x, seat in row.items():
            if is_occupied(seats, x, y):
                count += 1
    return count

def is_occupied(seats, x, y):
    seat = seats.get(y, {}).get(x)
    return seat == '#' 

def is_seat(seats, x, y):
    seat = seats.get(y, {}).get(x)
    return seat != '.'

def change(seats, fn, trigger):
    changed = False
    d = {}
    for y, row in seats.items():
        d[y] = {} 
        for x, seat in row.items():
            new_seat = seat
            if seat == 'L':
                if fn(seats, x, y) == 0:
                    new_seat = '#'
                    changed = True
            elif seat == '#':
                if fn(seats, x, y) > trigger:
                    new_seat = 'L'
                    changed = True
            d[y][x] = new_seat
    return (d, changed)

def part1(seats, xx, yy):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            x = xx + dx
            y = yy + dy

            if x == xx and y == yy:
                continue

            if is_occupied(seats, x, y):
                count += 1
    return count

def part2(seats, xx, yy):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            x = xx + dx
            y = yy + dy

            if x == xx and y == yy:
                continue 

            while not is_seat(seats, x, y):
                x += dx 
                y += dy
            
            if is_occupied(seats, x, y):
                count += 1
    return count

def boarding(seats, fn, trigger):
    changed = True
    new_seats = seats
    while changed:
        new_seats, changed = change(new_seats, fn, trigger)
    return count_occupied(new_seats)


if __name__ == '__main__':
    seats = {}
    with open('input') as file:
        seats = to_grid(map(lambda x: x.strip(), file))
        
    print(boarding(seats, part1, 3))
    print(boarding(seats, part2, 4))
