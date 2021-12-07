from functools import cache

crabs = []
with open('input') as file:
    crabs = list(map(int, next(file).strip().split(',')))


@cache
def sum_of_seq(n):
    return int((n * (n+1))/2)


lowest1 = None
lowest2 = None
for i in range(len(crabs)):
    p = i + 1

    total1 = 0
    total2 = 0
    for crab in crabs:
        steps = abs(crab - p)
        total1 += steps
        total2 += sum_of_seq(steps)

    if not lowest1:
        lowest1 = total1

    if not lowest2:
        lowest2 = total2

    if lowest1 > total1:
        lowest1 = total1

    if lowest2 > total2:
        lowest2 = total2

print('part 1')
print(lowest1)
print('part 2')
print(lowest2)
