from functools import cache

MOVES = [
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
]


def part1(D, **kwargs):
    rounds = kwargs["rounds"]
    m = [[ch for ch in D[i]] for i in range(len(D))]

    rows = len(m)
    cols = len(m[0])
    start = (0, 0)
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == "D":
                start = (r, c)
                break

    q = [(0, start[0], start[1])]
    seen = []
    seen.append((0, start[0], start[1]))
    ans = 0
    while q:
        t, row, col = q.pop()

        if t == rounds:
            continue
        for a, b in MOVES:
            r, c = (row + a, col + b)
            if (0 <= r < rows) and (0 <= c < cols) and ((t + 1, r, c) not in seen):
                if m[r][c] == "S":
                    m[r][c] = "X"
                    ans += 1
                q.append((t + 1, r, c))
                seen.append((t, r, c))

    return ans


def part2(D, **kwargs):
    rounds = kwargs["rounds"]
    m = [[ch for ch in D[i]] for i in range(len(D))]

    rows = len(m)
    cols = len(m[0])
    start = (0, 0)
    sheep = set()
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == "D":
                start = (r, c)
            elif m[r][c] == "S":
                sheep.add((r, c))
    q = [start]
    seen = set()
    seen.add(start)

    ans = 0
    for t in range(rounds):
        q = list(seen)
        while q:
            row, col = q.pop()
            for a, b in MOVES:
                r, c = (row + a, col + b)
                if (0 <= r < rows) and (0 <= c < cols) and ((r, c) not in seen):
                    seen.add((r, c))
            seen.remove((row, col))
        for r, c in seen:
            if m[r][c] == "#":
                continue
            if (r - t, c) in sheep:
                sheep.remove((r - t, c))
                ans += 1
            if (r - t - 1, c) in sheep:
                sheep.remove((r - t - 1, c))
                ans += 1
    return ans


def part3(D):
    m = [[ch for ch in D[i]] for i in range(len(D))]

    rows = len(m)
    cols = len(m[0])
    start = (0, 0)
    sheep = set()
    hideouts = set()
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == "D":
                start = (r, c)
            elif m[r][c] == "S":
                sheep.add((r, c))
            elif m[r][c] == "#":
                hideouts.add((r, c))
    seen = set()
    seen.add(start)

    sheep = list(sheep)

    def mask(pos):
        (row, col) = pos
        return 1 << (row * cols + col)

    def unmask(num):
        pos = num.bit_length() - 1
        return (pos // cols, pos % cols)

    sh = 0
    for s in sheep:
        sh |= mask(s)
    sheep = sh

    hide = 0
    for h in hideouts:
        hide |= mask(h)
    hideouts = hide

    @cache
    def rec(dragon, sheep, sheep_turn):
        if not sheep:
            return 1
        ans = 0
        if not sheep_turn:
            for a, b in MOVES:
                r, c = (dragon[0] + a, dragon[1] + b)
                if (0 <= r < rows) and (0 <= c < cols):
                    next = (r, c)
                    masked = mask(next)
                    if (masked & sheep) and not (masked & hideouts):
                        ans += rec(next, sheep & ~masked, not sheep_turn)
                    else:
                        ans += rec(next, sheep, not sheep_turn)
        else:
            moved = False
            for i in range(sheep.bit_length()):
                if not (sheep & 1 << i):
                    continue
                cur = unmask(1 << i)
                next = (cur[0] + 1, cur[1])
                if next == dragon and (mask(next) & ~hideouts):
                    continue
                moved = True
                if next[0] >= rows:
                    continue  # escaped
                ans += rec(dragon, (sheep | mask(next)) & ~mask(cur), not sheep_turn)
            if not moved:
                ans += rec(dragon, sheep, not sheep_turn)
        return ans

    return rec(start, sheep, True)


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(
        part1,
        part2,
        part3,
        example={"1": {"rounds": 3}, "2": {"rounds": 3}},
        input={"1": {"rounds": 4}, "2": {"rounds": 20}},
    )
