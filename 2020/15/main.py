def play(input, n):
    position = dict(map(lambda i: (i[1], [i[0]]), enumerate(input)))
    prev = input[-1]
    for i in range(len(input), n):
        if len(position[prev]) == 1:
            if position[prev][-1] == i - 1:
                prev = 0
        elif len(position[prev]) > 1:
            prev = position[prev][-1] - position[prev][-2]
        if not position.get(prev):
            position[prev] = []
        position[prev].append(i)
    return prev


if __name__ == "__main__":
    # input = [1, 2, 16, 19, 18, 0]
    input = [0, 3, 6]

    print(play(input, 2020))
    print(play(input, 30000000))
