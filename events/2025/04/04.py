def part1(D):
    gears = [int(x) for x in D]
    t = 2025

    k = 1.0
    for i in range(1, len(gears)):
        k *= gears[i - 1] / gears[i]
    return int(t * k)


def part2(D):
    gears = [int(x) for x in D]
    t = 10000000000000

    k = 1.0
    for i in range(1, len(gears)):
        k *= gears[i - 1] / gears[i]

    ans = t // k
    if t % k != 0:
        ans += 1

    return int(ans)


def part3(D):
    gears = [[int(x) for x in y.split("|")] for y in D]

    t = 100

    k = gears[0][0] / gears[1][0]
    for i in range(2, len(gears) - 1):
        k *= gears[i - 1][1] / gears[i][0]
    k *= gears[len(gears) - 2][1] / gears[len(gears) - 1][0]

    ans = int(t * k)
    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
