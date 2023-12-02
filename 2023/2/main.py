with open("input", "r") as file:
    data = file.read().splitlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# Part 1
possibles = []
for game in data:
    id, record = game.split(":")

    sets = record.split(";")

    possible = []
    for cubes in sets:
        matches = []
        for cube in cubes.split(","):
            count, color = cube.strip().split(" ")
            count = int(count)
            matches.append(bag[color] >= count)
        possible.append(all(matches))

    if all(possible):
        _, game_id = id.split(" ")
        possibles.append(int(game_id))

print(sum(possibles))

# Part 2

powers = []
for game in data:
    id, record = game.split(":")

    sets = record.split(";")

    combo = {"red": 0, "green": 0, "blue": 0}
    for cubes in sets:
        for cube in cubes.split(","):
            count, color = cube.strip().split(" ")
            count = int(count)
            if combo[color] < count:
                combo[color] = count
    powers.append(combo["red"] * combo["green"] * combo["blue"])

print(sum(powers))
