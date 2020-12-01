with open('input') as file:
    prev = []
    for row in file:
        raw = row.strip()
        if not raw:
            continue

        val = int(raw)

        found = False
        for x in prev:
            for y in prev:
                if x + y + val == 2020:
                    print(x * y * val)
                    found = True
                    break

            if found:
                break

        prev.append(val)
