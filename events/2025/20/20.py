from collections import Counter, defaultdict
from heapq import heappop, heappush


def parse_map(data):
    return [[ch for ch in data[i]] for i in range(len(data))]


def part1(D):
    m = parse_map(D)
    rows = len(m)
    cols = len(m[0])

    ans = 0
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == "T":
                if col > 0 and m[row][col - 1] == "T":
                    ans += 1
                if row > 0 and (row + col) % 2 == 0 and m[row - 1][col] == "T":
                    ans += 1

    return ans


def part2(D):
    m = parse_map(D)
    rows = len(m)
    cols = len(m[0])
    tr = defaultdict(list)

    s = (0, 0)
    e = (0, 0)
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == "S":
                s = (row, col)
                m[row][col] = "T"
            elif m[row][col] == "E":
                e = (row, col)
                m[row][col] = "T"
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == "T":
                if col > 0 and m[row][col - 1] == "T":
                    tr[(row, col - 1)].append((row, col))
                    tr[(row, col)].append((row, col - 1))
                if row > 0 and (row + col) % 2 == 0 and m[row - 1][col] == "T":
                    tr[(row - 1, col)].append((row, col))
                    tr[(row, col)].append((row - 1, col))

    q = [(0, s[0], s[1])]
    seen = {s}
    ans = 0
    while q:
        (cost, row, col) = heappop(q)
        if (row, col) == e:
            ans = cost
            break
        for next in tr[(row, col)]:
            if next not in seen:
                heappush(q, (cost + 1, next[0], next[1]))
                seen.add(next)

    return ans


def part3(D):
    m = parse_map(D)
    rows = len(m)
    cols = len(m[0])

    tr = defaultdict(list)

    s = (0, 0)
    e = (0, 0)
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == "S":
                s = (row, col)
                m[row][col] = "T"
            elif m[row][col] == "E":
                e = (row, col)
                m[row][col] = "T"

    def down_line():
        tg = []
        for row in reversed(range(rows)):
            for col in range(cols):
                if m[row][col] != ".":
                    tg.append((row, col))
        return tg

    def left_line():
        tg = []
        sr = 0
        for sc in range(0, cols, 2):
            row = sr
            col = sc
            while row < rows and col >= 0:
                if m[row][col] == ".":
                    break
                tg.append((row, col))
                if col > 0:
                    col -= 1
                    if m[row][col] == ".":
                        break
                    tg.append((row, col))
                row += 1
        return tg

    def right_line():
        tg = []
        sc = cols
        for sr in range(rows):
            sc -= 1
            row = sr
            col = sc
            tg.append((row, col))
            row -= 1
            while row >= 0 and col >= 0:
                if m[row][col] == ".":
                    break
                tg.append((row, col))
                if col > 0:
                    col -= 1
                    if col < 0 or m[row][col] == ".":
                        break
                    tg.append((row, col))
                row -= 1
        return tg

    down = down_line()
    left = left_line()
    right = right_line()
    assert Counter(down) == Counter(left) == Counter(right)

    ld = len(down)
    nb = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            if col > 0:
                nb[(row, col - 1)].append((row, col))
                nb[(row, col)].append((row, col - 1))
            if row > 0 and (row + col) % 2 == 0:
                nb[(row - 1, col)].append((row, col))
                nb[(row, col)].append((row - 1, col))

    all = [down, right, left]
    for id in range(3):
        next_id = (id + 1) % 3
        for i in range(ld):
            row, col = all[id][i]
            if m[row][col] != "T":
                continue
            r, c = all[next_id][i]
            if m[r][c] == "T":
                tr[(row, col)].append((r, c))
            for neigh in nb[(r, c)]:
                if m[neigh[0]][neigh[1]] == "T":
                    tr[(row, col)].append((neigh[0], neigh[1]))

    q = [(0, s[0], s[1])]
    seen = {s}
    ans = 0
    while q:
        (cost, row, col) = heappop(q)
        if (row, col) == e:
            ans = cost
            break
        for next in tr[(row, col)]:
            if next not in seen:
                heappush(q, (cost + 1, next[0], next[1]))
                seen.add(next)

    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
