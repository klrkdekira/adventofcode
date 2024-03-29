measurements = []
with open("input") as file:
    measurements = list(map(lambda l: int(l.strip()), file))


def find_delta(dataset):
    deltas = []
    for i, value in enumerate(dataset):
        if i == 0:
            continue
        deltas.append(value - dataset[i - 1])
    return deltas


def count_increased(deltas):
    return len(list(filter(lambda x: x > 0, deltas)))


def group_window(dataset):
    sums = []
    i = 0
    while i < len(dataset):
        a = i
        b = i + 1
        c = i + 2

        if c >= len(dataset):
            break

        sums.append(dataset[a] + dataset[b] + dataset[c])
        i += 1
    return sums


print("part 1")
print(count_increased(find_delta(measurements)))
print("part 2")
print(count_increased(find_delta(group_window(measurements))))
