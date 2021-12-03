report = []
with open('input') as file:
    report = list(map(lambda x: x.strip(), file))

gamma = ''
epsilon = ''
for bits in zip(*report[::1]):
    zero = 0
    one = 0
    for bit in bits:
        if bit == '1':
            one += 1
        else:
            zero += 1

    if one > zero:
        gamma += '1'
        epsilon += '0'
    elif zero > one:
        gamma += '0'
        epsilon += '1'

print('part 1')
print(int(gamma, 2) * int(epsilon, 2))


def get_rating(initial, weight):
    p = initial
    for i in range(len(p[0])):
        one = []
        zero = []
        for row in p:
            if row[i] == '1':
                one.append(row)
            else:
                zero.append(row)

        if len(one) > len(zero):
            if weight == '1':
                p = one
            else:
                p = zero
        elif len(zero) > len(one):
            if weight == '1':
                p = zero
            else:
                p = one
        else:
            if weight == '1':
                p = one
            else:
                p = zero

        if len(p) == 1:
            return p[0]


o2 = get_rating(report, '1')
co2 = get_rating(report, '0')
print('part 2')
print(int(o2, 2) * int(co2, 2))
