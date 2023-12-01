with open("input", "r") as file:
    data = file.read().splitlines()

# Part 1
values = []

for line in data:
    digits = [int(v) for v in line if v.isdigit()]
    values.append(int(f"{digits[0]}{digits[-1]}"))

print(sum(values))

# Part 2
values = []

for line in data:
    digits = []
    prev = ""
    for v in line:
        if v.isdigit():
            digits.append(v)
            prev = ""
        else:
            prev += v
            if "one" in prev:
                digits.append("1")
                prev = v
            elif "two" in prev:
                digits.append("2")
                prev = v
            elif "three" in prev:
                digits.append("3")
                prev = v
            elif "four" in prev:
                digits.append("4")
                prev = v
            elif "five" in prev:
                digits.append("5")
                prev = v
            elif "six" in prev:
                digits.append("6")
                prev = v
            elif "seven" in prev:
                digits.append("7")
                prev = v
            elif "eight" in prev:
                digits.append("8")
                prev = v
            elif "nine" in prev:
                digits.append("9")
                prev = v
    values.append(int(f"{digits[0]}{digits[-1]}"))

print(sum(values))
