import re


def int_to_bin(i, pad):
    return "{0:b}".format(int(i)).rjust(pad, "0")


def parse_mask(line):
    mask = line.split("=")[1].strip()
    replacement = list(enumerate(mask))
    return ("mask", replacement)


pattern = re.compile("^mem\[(\d+)\] = (\d+)$")


def parse_value(line):
    addr, value = pattern.findall(line)[0]
    return ("value", (int_to_bin(addr, 36), int_to_bin(value, 36)))


def parse(line):
    if "mask" in line:
        return parse_mask(line)
    return parse_value(line)


def mask_value(program):
    results = {}
    mask = []
    for (cmd, data) in program:
        if cmd == "mask":
            mask = list(filter(lambda i: i[1] != "X", data))
            continue

        addr, value = data
        for (i, bit) in mask:
            value = value[:i] + bit + value[i + 1 :]

        if not results.get(addr):
            results[addr] = 0
        results[addr] = int(value, 2)
    return sum(results.values())


def mask_address(program):
    results = {}
    mask = []
    for (cmd, data) in program:
        if cmd == "mask":
            mask = data
            continue

        addr, value = data

        floats = []
        for (i, bit) in mask:
            if bit == "0":
                continue

            addr = addr[:i] + bit + addr[i + 1 :]
            if bit == "X":
                floats.append(i)

        for i in range(2 ** len(floats)):
            drops = int_to_bin(i, len(floats))
            new_addr = addr
            for (j, bit) in enumerate(drops):
                position = floats[j]
                new_addr = new_addr[:position] + bit + new_addr[position + 1 :]

            if not results.get(new_addr):
                results[new_addr] = 0
            results[new_addr] = int(value, 2)
    return sum(results.values())


if __name__ == "__main__":
    program = []
    with open("input") as file:
        program = list(map(parse, file))

    print(mask_value(program))
    print(mask_address(program))
