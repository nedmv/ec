def part1(D):
    names = D[0].split(",")
    n = len(names)
    pos = 0
    for s in D[2].split(","):
        num = int(s[1:])
        dir = s[0]
        if dir == "L":
            pos = max(0, pos - num)
        else:
            pos = min(n - 1, pos + num)

    return names[pos]


def part2(D):
    names = D[0].split(",")
    n = len(names)
    pos = 0
    for s in D[2].split(","):
        num = int(s[1:])
        dir = s[0]
        if dir == "L":
            pos = (pos - num + n) % n
        else:
            pos = (pos + num + n) % n

    return names[pos]


def part3(D):
    names = D[0].split(",")
    n = len(names)
    pos = 0
    for s in D[2].split(","):
        num = int(s[1:])
        dir = s[0]

        if dir == "L":
            pos = (n - num) % n
        else:
            pos = (num + n) % n
        names[0], names[pos] = names[pos], names[0]

    return names[0]


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
