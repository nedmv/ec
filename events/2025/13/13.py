from collections import deque


def part1(D):
    t = 2025
    nums = [int(x) for x in D]
    n = len(nums)
    round = deque([1])
    clockwise = True
    for num in nums:
        if clockwise:
            round.append(num)
        else:
            round.appendleft(num)
        clockwise = not clockwise
    start = 0
    for i in range(n + 1):
        if round[i] == 1:
            start = i
            break
    id = (start + t) % (n + 1)
    return round[id]


def solve(D, t):
    ans = 0
    nums = [[int(x) for x in y.split("-")] for y in D]
    n = len(nums)
    round = deque([(1, 1, 1)])
    clockwise = True
    for l, r in nums:
        k = r - l + 1
        if clockwise:
            round.append((k, l, r))
        else:
            round.appendleft((k, l, r))
        clockwise = not clockwise

    left_len = 0
    for i in range(n + 1):
        if round[i][0] == 1:
            break
        left_len += round[i][0]
    total_len = sum([r[0] for r in round])
    id = (left_len + t) % total_len

    cur = -1
    for i in range(n + 1):
        cur += round[i][0]
        d = cur - id
        if d >= 0:
            if id <= left_len:
                ans = round[i][1] + d
            else:
                ans = round[i][2] - d
            break

    return ans


def part2(D):
    return solve(D, 20252025)


def part3(D):
    return solve(D, 202520252025)

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
