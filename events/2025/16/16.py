def part1(D):
    ints = [int(x) for x in D[0].split(",")]
    cols = 90
    ans = 0
    for num in ints:
        ans += cols // num
    return ans


def part2(D):
    ints = [int(x) - 1 for x in D[0].split(",")]
    n = len(ints)
    ans = 1

    for t in range(2, n + 1):
        success = True
        for i in range(t - 1, n, t):
            if ints[i] == 0:
                success = False
                break
        if success:
            for i in range(t - 1, n, t):
                ints[i] -= 1
            ans *= t
    return ans


def part3(D):
    blocks = 202520252025000
    ints = [int(x) - 1 for x in D[0].split(",")]
    n = len(ints)

    ans = 1
    spell = [1]
    for t in range(2, n + 1):
        success = True
        for i in range(t - 1, n, t):
            if ints[i] == 0:
                success = False
                break
        if success:
            for i in range(t - 1, n, t):
                ints[i] -= 1
            spell.append(t)

    def can_build(cols):
        total = blocks
        for s in spell:
            total -= cols // s
            if total < 0:
                return False
        return True

    l = 1
    r = blocks
    while l <= r:
        m = (r + l) // 2
        if can_build(m):
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
