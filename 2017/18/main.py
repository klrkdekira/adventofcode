def parse(line):
    parts = line.strip().split()
    steps = ""
    if len(parts) == 3:
        steps = parts[2]
    return (parts[0], parts[1], steps)


def recover(program):
    vms = {}
    i = 0
    played = 0
    while True:
        op, vm, steps = program[i]
        n = int(vms.get(vm, 0))

        if op == "set":
            vms[vm] = int(vms.get(steps, steps))
        elif op == "add":
            n += int(vms.get(steps, steps))
            vms[vm] = n
        elif op == "mul":
            n *= int(vms.get(steps, steps))
            vms[vm] = n
        elif op == "mod":
            n %= int(vms.get(steps, steps))
            vms[vm] = n
        elif op == "rcv":
            if n > 0:
                return played
        elif op == "jgz":
            if n > 0:
                i += int(vms.get(steps, steps))
                continue
        elif op == "snd":
            played = n
        i += 1


def run(program, vm, p):
    i = 0
    sent = 0

    yield

    while True:
        op, key, steps = program[i]
        n = vm.get(key, 0)

        if op == "set":
            vm[key] = int(vm.get(steps, steps))
        elif op == "add":
            n += int(vm.get(steps, steps))
            vm[key] = n
        elif op == "mul":
            n *= int(vm.get(steps, steps))
            vm[key] = n
        elif op == "mod":
            n %= int(vm.get(steps, steps))
            vm[key] = n
        elif op == "rcv":
            yield ("rcv", key, sent)
            yield
        elif op == "jgz":
            if n > 0:
                i += int(vm.get(steps, steps))
                continue
        elif op == "snd":
            sent += 1

            yield ("snd", int(vm.get(key, steps)), sent)
            yield
        i += 1


def phone(program):
    r1 = {}
    r2 = {}

    vm1 = run(program, r1, 0)
    vm2 = run(program, r2, 0)

    status1 = {"snd": [], "rcv": []}
    status2 = {"snd": [], "rcv": []}

    count = 0
    while True:
        if (len(status2["snd"]) == 0 and len(status1["rcv"]) > 0) and (
            len(status1["snd"]) == 0 and len(status2["rcv"]) > 0
        ):
            break

        if len(status1["rcv"]) > 0:
            if len(status2["snd"]) > 0:
                _, key, _ = status1["rcv"][0]
                _, i, _ = status2["snd"][0]

                print("replaced", 0, key, i)
                r1[key] = i

                status1["rcv"] = status1["rcv"][1:]
                status2["snd"] = status2["snd"][1:]

        if len(status2["rcv"]) > 0:
            if len(status1["snd"]) > 0:
                _, key, _ = status2["rcv"][0]
                _, i, _ = status1["snd"][0]

                print("replaced", 1, key, i)
                r2[key] = i

                status2["rcv"] = status2["rcv"][1:]
                status1["snd"] = status1["snd"][1:]

        next(vm1)
        data = next(vm1)
        status1[data[0]].append(data)

        next(vm2)
        data = next(vm2)
        status2[data[0]].append(data)

        # print(status1)
        # print(status2)

        # status2.append(next(vm2))

        # if status1[0] == "rcv" and status2[0] == "rcv":
        #     break

    return count


if __name__ == "__main__":
    with open("input") as file:
        program = list(map(parse, file))
        # print(recover(program))
        print(phone(program))
