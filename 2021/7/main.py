crabs = []
with open('input') as file:
    crabs = list(map(int, next(file).strip().split(',')))


lower = 0
for i in range(len(crabs)):
    p = i + 1
    total = 0
    for crab in crabs:
        total += abs(crab - p)

    if lower == 0:
        lower = total

    if total < lower:
        lower = total

print('part 1')
print(lower)


def sum_of_seq(n):
    return int((n * (n+1))/2)


lower = 0
for i in range(len(crabs)):
    p = i + 1
    total = 0
    for crab in crabs:
        total += sum_of_seq(abs(crab - p))

    if lower == 0:
        lower = total

    if total < lower:
        lower = total

print('part 2')
print(lower)
