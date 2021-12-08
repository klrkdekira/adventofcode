entries = []


def parse(line):
    return list(map(lambda x: tuple(x.strip().split(' ')), line.strip().split('|')))


with open("input") as file:
    entries = list(map(parse, file))

count = 0
total = 0
for segments, outputs in entries:
    dict = {}

    for segment in segments:
        length = len(segment)
        if length == 2:
            dict[1] = segment
        elif length == 4:
            dict[4] = segment
        elif length == 3:
            dict[7] = segment
        elif length == 7:
            dict[8] = segment

    num = ''
    for output in outputs:
        length = len(output)
        if length == 2:
            num += '1'
            count += 1
        elif length == 4:
            num += '4'
            count += 1
        elif length == 3:
            num += '7'
            count += 1
        elif length == 7:
            num += '8'
            count += 1
        elif length == 5:
            if len(set(output).intersection(dict[1])) == 2:
                num += '3'
            elif len(set(output).intersection(dict[4])) == 2:
                num += '2'
            else:
                num += '5'
        elif length == 6:
            if len(set(output).intersection(dict[1])) == 1:
                num += '6'
            elif len(set(output).intersection(dict[4])) == 4:
                num += '9'
            else:
                num += '0'
    total += int(num)

print('part 1')
print(count)
print("part 2")
print(total)
