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
        if not v:
            continue
        if k in rules:
            left = k[0], rules[k]
            right = rules[k], k[1]
            changes[k] -= v
            changes[left] += v
            changes[right] += v

    for k, v in changes.items():
        if not v:
            continue
        polymer[k] += v


def summarise(polymer):
    summary = defaultdict(int)
    for k, v in polymer.items():
        summary[k[1]] += v
    return max(summary.values()) - min(summary.values())


for i in range(40):
    insertion(template)
    if i == 9:
        print("part 1")
        print(summarise(template))

print("part 2")
print(summarise(template))
