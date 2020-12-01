with open('input') as file:
    prev = []
    for row in file:
        raw = row.strip()
        if not raw:
            continue

        val = int(raw)

        for i in prev:
            if i + val == 2020:
                print(i * val)
                break

        prev.append(val)
