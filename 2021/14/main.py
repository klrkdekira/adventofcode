from collections import defaultdict

raw_template = []
rules = []

with open("input") as file:
    raw_template = list(next(file).strip())
    for line in file:
        line = line.strip()
        if not line:
            continue
        left, right = line.split("->")
        left = left.strip()
        right = right.strip()
        rules.append(((left[0], left[1]), right))
    rules = dict(rules)

template = defaultdict(int)
for i, v in enumerate(raw_template):
    if i == 0:
        continue
    key = raw_template[i - 1], v
    if key in rules:
        template[key] += 1


def insertion(polymer):
    changes = defaultdict(int)
    for k, v in polymer.items():
        if v == 0:
            continue
        if k in rules:
            left = k[0], rules[k]
            right = rules[k], k[1]
            changes[k] -= v
            changes[left] += v
            changes[right] += v
    for k, v in changes.items():
        polymer[k] += v


def summarise(polymer):
    summary = defaultdict(int)
    for k, v in polymer.items():
        a, b = k
        summary[a] += v / 2
        summary[b] += v / 2
    values = sorted(summary.values())
    return int(values[len(values) - 1] - values[0])


for i in range(40):
    insertion(template)
    if i == 9:
        print("part 1")
        print(summarise(template))

print("part 2")
print(summarise(template))
