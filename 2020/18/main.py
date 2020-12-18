operators = [
    "+",
    "-",
    "*",
    "/",
]


def parse(line, priority=""):
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    stack, p = [], []

    expressions = line.split()
    for i in expressions:
        if i == "(":
            stack.append(i)
            continue

        if i.endswith(")"):
            while len(stack) > 0 and stack[-1] != "(":
                p.append(stack.pop())
            stack.pop()
            continue

        if i in operators:
            if (len(stack) == 0) or (len(stack) > 0 and stack[-1] == "("):
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1] != "(" and i != priority:
                    popped = stack.pop()
                    p.append(popped)
                stack.append(i)
            continue

        p.append(i)

    while len(stack) > 0:
        p.append(stack.pop())

    return p


def compute(line, priority=""):
    parsed = parse(line, priority)

    stack = []
    for p in parsed:
        if p in operators:
            a = int(stack.pop())
            b = int(stack.pop())

            c = 0
            if p == "+":
                c = b + a
            elif p == "-":
                c = b - a
            elif p == "*":
                c = b * a
            elif p == "/":
                c = b / a

            stack.append(c)
            continue
        stack.append(p)

    return stack.pop()


if __name__ == "__main__":
    lines = []
    with open("input") as file:
        lines = [line.strip() for line in file]

    print(sum(map(lambda line: compute(line, ""), lines)))
    print(sum(map(lambda line: compute(line, "+"), lines)))
