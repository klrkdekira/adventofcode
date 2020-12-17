from itertools import product, repeat


def parse(file, dimension=3):
    d = {}
    for (i, y) in enumerate(file):
        y = y.strip()
        for (j, x) in enumerate(y):
            key = tuple([j, i] + [0] * (dimension - 2))
            d[key] = x == "#"
    return d


neighbours = {
    3: [p for p in product([-1, 0, 1], repeat=3) if p != (0, 0, 0)],
    4: [p for p in product([-1, 0, 1], repeat=4) if p != (0, 0, 0, 0)],
}


def find_neighbours(cubes, cube, dimension=3):
    count = 0
    for n in neighbours[dimension]:
        if cubes.get(tuple(map(sum, zip(cube, n)))):
            count += 1
    return count


def move(cubes, dimension=3):
    expands = []
    for cube in cubes:
        for n in neighbours[dimension]:
            c = tuple(map(sum, zip(cube, n)))
            if c not in cubes:
                expands.append(c)

    for cube in expands:
        cubes[cube] = False

    new_cubes = {}
    for (cube, b) in cubes.items():
        count = find_neighbours(cubes, cube, dimension)
        if b:
            new_cubes[cube] = count in [2, 3]
        else:
            new_cubes[cube] = count == 3
    return new_cubes


def boot(cubes, dimension=3):
    for i in range(6):
        cubes = move(cubes, dimension)
    return len(list(filter(lambda cube: cube[1] == True, cubes.items())))


if __name__ == "__main__":
    cubes = {}
    with open("test") as file:
        cubes = parse(file)

    print(boot(cubes, dimension=3))
    cubes = dict(map(lambda c: (tuple(list(c[0]) + [0]), c[1]), cubes.items()))
    print(boot(cubes, dimension=4))
