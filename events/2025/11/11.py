def part1(D):
    ans = 0
    time = 10

    ducks = [int(x) for x in D]
    n = len(ducks)

    moved = True
    t = 0
    while moved:
        moved = False
        for i in range(1, n):
            if ducks[i - 1] > ducks[i]:
                ducks[i - 1] -= 1
                ducks[i] += 1
                moved = True
        if moved:
            t += 1

    moved = True
    for _ in range(time - t):
        for i in range(1, n):
            if ducks[i - 1] < ducks[i]:
                ducks[i - 1] += 1
                ducks[i] -= 1
                moved = True

    for i in range(n):
        ans += (i + 1) * ducks[i]
    return ans


def part2(D):
    ducks = [int(x) for x in D]
    n = len(ducks)

    moved = True
    t = 0
    while moved:
        moved = False
        for i in range(1, n):
            if ducks[i - 1] > ducks[i]:
                ducks[i - 1] -= 1
                ducks[i] += 1
                moved = True
        if moved:
            t += 1

    moved = True
    while moved:
        moved = False
        for i in range(1, n):
            if ducks[i - 1] < ducks[i]:
                ducks[i - 1] += 1
                ducks[i] -= 1
                moved = True
        if moved:
            t += 1

    return t


def part3(D):
    ducks = [int(x) for x in D]
    n = len(ducks)

    for i in range(1, n):
        assert ducks[i - 1] <= ducks[i]

    t = sum(ducks) // n
    ans = 0
    for i in range(n):
        ans += abs(ducks[i] - t)

    return ans // 2


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
