with open('input') as file:
    prev = []

    found_twins = False
    found_triplets = False

    for val in map(int, map(lambda i: i.strip(), file)):
        for x in prev:
            if not found_twins and x + val == 2020:
                print('twins', x * val)
                found_twins = True

            for y in prev:
                if not found_triplets and x + y + val == 2020:
                    print('triplets', x * y * val)
                    found_triplets = True

                if found_triplets:
                    break

        if found_twins and found_triplets:
            break

        prev.append(val)
