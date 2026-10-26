def part1(D):
    ints = [int(x) for x in D[0].split(",")]
    ints.sort(reverse=True)
    cur = ints[0]
    ans = cur
    for i in range(1, len(ints)):
        if ints[i] < cur:
            cur = ints[i]
            ans += cur
    return ans


def part2(D):
    ints = [int(x) for x in D[0].split(",")]
    ints.sort()
    cur = ints[0]
    ans = cur
    cnt = 1
    for i in range(1, len(ints)):
        if ints[i] > cur:
            cur = ints[i]
            ans += cur
            cnt += 1
            if cnt == 20:
                break
    return ans


def part3(D):
    ints = [int(x) for x in D[0].split(",")]
    ints.sort()

    cur = -1
    cnt = 1
    max_cnt = 1
    for num in ints:
        if num == cur:
            cnt += 1
        else:
            cur = num
            cnt = 1
        max_cnt = max(cnt, max_cnt)

    return max_cnt


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
