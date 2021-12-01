operators = [
    "+",
    "-",
    "*",
    "/",
]


def parse(line, precedence=None):
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    stack, p = [], []

    for i in line.split():
        if i == "(":
            stack.append(i)
            continue

        if i == ")":
            while len(stack) > 0 and stack[-1] != "(":
                p.append(stack.pop())
            stack.pop()
            continue

        if i in operators:
            if (len(stack) == 0) or (len(stack) > 0 and stack[-1] == "("):
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1] != "(" and i not in precedence:
                    popped = stack.pop()
                    p.append(popped)
                stack.append(i)
            continue

        p.append(i)

    while len(stack) > 0:
        p.append(stack.pop())

    return p


def compute(line, precedence=None):
    parsed = parse(line, precedence)

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

    print(sum(map(lambda line: compute(line, []), lines)))
    print(sum(map(lambda line: compute(line, ["+"]), lines)))
    print(sum(map(lambda line: compute(line, ["*", "/"]), lines)))
