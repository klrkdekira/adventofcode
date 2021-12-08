entries = []


def parse(line):
    entry = []
    for part in line.strip().split("|"):
        entry.append(
            tuple(map(lambda x: "".join(sorted(x.strip())), part.strip().split(" ")))
        )
    return entry


with open("input") as file:
    entries = list(map(parse, file))

panel = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

panel_lookup = {v: k for k, v in panel.items()}

outputs = list(map(lambda x: x[1], entries))

target = [
    len(panel[1]),
    len(panel[4]),
    len(panel[7]),
    len(panel[8]),
]

count = 0
for output in outputs:
    for value in output:
        if len(value) in target:
            count += 1

print("part 1")
print(count)

total = 0
for segments, output in entries:
    d = {}

    rest = []

    for s in segments:
        l = len(s)
        if l == 2:
            d[1] = s
        elif l == 4:
            d[4] = s
        elif l == 3:
            d[7] = s
        elif l == 7:
            d[8] = s
        else:
            rest.append(s)

    while len(rest) > 0:
        for s in rest:
            if len(s) == 6:
                matched = 0
                for i in [1, 4, 7]:
                    if len(set(s).intersection(d[i])) == len(d[i]):
                        matched += 1
                if matched == 0:
                    d[6] = s
                    rest.remove(s)
                elif matched == 2:
                    d[0] = s
                    rest.remove(s)
                elif matched == 3:
                    d[9] = s
                    rest.remove(s)
            elif len(s) == 5:
                matched = 0
                for i in [1, 7]:
                    if len(set(s).intersection(d[i])) == len(d[i]):
                        matched += 1

                if matched == 2:
                    d[3] = s
                    rest.remove(s)
                    continue

                if 6 in d:
                    if len(set(s).intersection(d[6])) == len(d[6]) - 1:
                        d[5] = s
                        rest.remove(s)
                        continue
                    else:
                        d[2] = s
                        rest.remove(s)
                        continue

    reversed = {v: str(k) for k, v in d.items()}

    num = ""
    for o in output:
        num += reversed[o]
    total += int(num)

print("part 2")
print(total)
