def find_sum(list, n):
    for (i, p) in enumerate(list):
        for (j, q) in enumerate(list):
            if i == j:
                continue

            if p + q == n:
                return True
    return False


def part1(list, n):
    prev = list[:n]
    for i in list[n:]:
        if not find_sum(prev, i):
            return i
        prev.append(i)


def part2(list, invalid):
    nums = []
    pair = ()
    for (i, n) in enumerate(list):
        nums.append(n)
        p = 0
        while p < len(nums):
            if p != i:
                nums[p] += n
                if nums[p] == invalid:
                    pair = (p, i)
                    break
            p += 1
    z = sorted(list[pair[0] : pair[1]])
    return z[0] + z[-1]


if __name__ == "__main__":
    with open("input") as file:
        rows = list(map(int, file))
        invalid = part1(rows, 25)
        print(invalid)
        print(part2(rows, invalid))
