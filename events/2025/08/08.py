def part1(D, **kwargs):
    n = kwargs["n"]
    nails = [int(x) for x in D[0].split(",")]
    ans = 0
    for i in range(len(nails) - 1):
        if abs(nails[i + 1] - nails[i]) == n // 2:
            ans += 1

    return ans


def part2(D, **kwargs):
    nails = [int(x) for x in D[0].split(",")]
    ans = 0

    pairs = []
    for i in range(len(nails) - 1):
        a, b = sorted([nails[i], nails[i + 1]])
        for x, y in pairs:
            if a <= x <= b and a <= y <= b:
                pass
            elif (x <= a or x >= b) and (y <= a or y >= b):
                pass
            else:
                ans += 1
        pairs.append((a, b))

    return ans


def part3(D, **kwargs):
    n = kwargs["n"]
    nails = [int(x) for x in D[0].split(",")]
    ans = 0

    pairs = []
    for i in range(len(nails) - 1):
        a, b = sorted([nails[i], nails[i + 1]])
        pairs.append((a, b))

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            cur = 0
            for x, y in pairs:
                if a == x and b == y:
                    cur += 1
                elif a <= x <= b and a <= y <= b:
                    pass
                elif (x <= a or x >= b) and (y <= a or y >= b):
                    pass
                else:
                    cur += 1
            ans = max(ans, cur)

    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(
        part1,
        part2,
        part3,
        example={"1": {"n": 8}, "2": {"n": 8}, "3": {"n": 8}},
        input={"1": {"n": 32}, "2": {"n": 32}, "3": {"n": 256}},
    )
