fish = {i: 0 for i in range(9)}

with open("input") as file:
    for i in map(int, next(file).split(",")):
        fish[i] += 1


for day in range(256):
    prev = None
    babies = 0
    for i in reversed(range(9)):
        now = fish[i]
        fish[i] = prev
        prev = now
        if i == 0:
            babies = now
    fish[6] = fish[6] + prev
    fish[8] = babies

    if day == 79:
        print("part 1")
        print(sum(fish.values()))

print("part 2")
print(sum(fish.values()))
