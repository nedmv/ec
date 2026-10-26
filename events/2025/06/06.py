def part1(D):
    ans = 0
    data = D[0]
    mentors = 0
    for ch in data:
        if ch == "a":
            ans += mentors
        elif ch == "A":
            mentors += 1
    return ans


def part2(D):
    ans = 0
    data = D[0]
    mentors = [0, 0, 0]
    for ch in data:
        if ch == "a":
            ans += mentors[0]
        elif ch == "b":
            ans += mentors[1]
        elif ch == "c":
            ans += mentors[2]
        elif ch == "A":
            mentors[0] += 1
        elif ch == "B":
            mentors[1] += 1
        elif ch == "C":
            mentors[2] += 1
    return ans


def part3(D):
    ans = 0
    data = D[0]
    n = len(data)
    mentors = [0, 0, 0]

    for i in range(999):
        ch = data[i % n]
        match ch:
            case "A":
                mentors[0] += 1
            case "B":
                mentors[1] += 1
            case "C":
                mentors[2] += 1

    def add_mentor(i):
        ch = data[i % n]
        match ch:
            case "A":
                mentors[0] += 1
            case "B":
                mentors[1] += 1
            case "C":
                mentors[2] += 1

    def remove_mentor(i):
        ch = data[i % n]
        match ch:
            case "A":
                mentors[0] -= 1
            case "B":
                mentors[1] -= 1
            case "C":
                mentors[2] -= 1

    for i in range(1000 * n):
        if i < 1000 * (n - 1):
            add_mentor(i + 1000)

        ch = data[i % n]
        if ch == "a":
            ans += mentors[0]
        elif ch == "b":
            ans += mentors[1]
        elif ch == "c":
            ans += mentors[2]

        if i >= 1000:
            remove_mentor(i - 1000)

    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
