import heapq

grid = []
with open("input") as file:
    grid = list(map(lambda x: x.strip(), file))


def lookup(grid, p=(0, 0)):
    return int(grid[p[1]][p[0]])


adjacent = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def find_neighbours(grid, start=(0, 0)):
    x, y = start

    n = []
    for dx, dy in adjacent:
        x1, y1 = x + dx, y + dy

        if y1 >= 0 and y1 < len(grid) and x1 >= 0 and x1 < len(grid[y1]):
            n.append((x1, y1))
    return n


def find_exit(grid):
    x, y = 0, 0
    y = len(grid) - 1
    x = len(grid[y]) - 1
    return x, y


def search(grid):
    start = (0, 0)
    end = find_exit(grid)

    history = {}
    history[start] = None

    cost = {}
    cost[start] = 0

    pq = [(0, start)]

    while pq:
        _, current = heapq.heappop(pq)
        if current == end:
            break
        for n in find_neighbours(grid, current):
            new_cost = cost[current] + lookup(grid, n)
            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                heapq.heappush(pq, (new_cost, n))
                history[n] = current
    return history, cost, cost[end]


def expand(grid):
    new_grid = []

    for y in range(5):
        for row in grid:
            new_row = ""
            for x in range(5):
                for col in row:
                    c = (int(col) + x + y - 1) % 9 + 1
                    new_row += str(c)
            new_grid.append(new_row)
    return new_grid


print("part 1")
history, cost, total_cost = search(grid)
print(total_cost)

print("part 2")
history, cost, total_cost = search(expand(grid))
print(total_cost)
