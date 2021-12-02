def parse_command(data):
    direction, steps = data.strip().split(" ")
    return (
        direction,
        int(steps),
    )


cmds = []
with open("input") as input:
    cmds = list(map(parse_command, input))

horizontal = 0
depth = 0
for cmd in cmds:
    direction, steps = cmd
    if direction == "forward":
        horizontal += steps
    elif direction == "down":
        depth += steps
    elif direction == "up":
        depth -= steps

print("part 1")
print(horizontal * depth)

horizontal = 0
depth = 0
aim = 0
for cmd in cmds:
    direction, steps = cmd
    if direction == "forward":
        horizontal += steps
        depth += aim * steps
    elif direction == "down":
        aim += steps
    elif direction == "up":
        aim -= steps

print("part 2")
print(horizontal * depth)
