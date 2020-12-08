def parse(cmd):
    ins, steps = cmd.strip().split()
    return (ins, int(steps))


def boot_error(cmds):
    i = 0
    history = []
    acc = 0
    while True:
        if i in history:
            break
        history.append(i)
        cmd, steps = cmds[i]
        if cmd == "acc":
            acc += steps
        elif cmd == "jmp":
            i += steps
            continue
        i += 1
    return acc


def boot_fix(cmds, verbose=False):
    i = 0
    acc = 0

    history = []
    changes = []
    flipped = False
    while i < len(cmds):
        if i in history:
            i = 0
            acc = 0
            history = []
            flipped = False
            if verbose:
                print("")
        history.append(i)

        cmd, steps = cmds[i]

        if verbose:
            print(cmd, steps, acc)

        if cmd == "acc":
            acc += steps
        if cmd == "nop":
            if i not in changes and not flipped:
                if verbose:
                    print("change nop to jmp", steps)
                changes.append(i)
                i += steps
                flipped = True
                continue
        elif cmd == "jmp":
            if i not in changes and not flipped:
                if verbose:
                    print("change jmp to nop")
                changes.append(i)
                i += 1
                flipped = True
                continue
            i += steps
            continue
        i += 1
    return acc


if __name__ == "__main__":
    with open("input") as file:
        cmds = list(map(parse, file))
        print(boot_error(cmds))
        print(boot_fix(cmds))
