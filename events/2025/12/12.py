moves = [1, 0, -1, 0, 1]


def copy2d(a: list[list]):
    return [[a[r][c] for c in range(len(a[0]))] for r in range(len(a))]


def count2d(seen: list[list]):
    return sum([sum(x) for x in seen])


def solve(D, part2=False):
    rows = len(D)
    cols = len(D[0])

    q = [(0, 0)]
    if part2:
        q.append((rows - 1, cols - 1))

    seen = [[False for _ in range(cols)] for _ in range(rows)]
    while q:
        row, col = q.pop()

        for i in range(4):
            r = row + moves[i]
            c = col + moves[i + 1]
            if (
                0 <= r < rows
                and 0 <= c < cols
                and D[r][c] <= D[row][col]
                and not seen[r][c]
            ):
                seen[r][c] = True
                q.append((r, c))

    return count2d(seen)


def part1(D):
    return solve(D)


def part2(D):
    return solve(D, part2=True)


def part3(D):
    rows = len(D)
    cols = len(D[0])

    def find_best(start_seen):
        best = 0
        best_pos = (0, 0)
        best_seen = [[]]
        for sr in range(rows):
            for sc in range(cols):
                q = [(sr, sc)]
                seen = copy2d(start_seen)
                seen[sr][sc] = True
                while q:
                    row, col = q.pop()

                    for i in range(4):
                        r = row + moves[i]
                        c = col + moves[i + 1]
                        if (
                            0 <= r < rows
                            and 0 <= c < cols
                            and D[r][c] <= D[row][col]
                            and not seen[r][c]
                        ):
                            seen[r][c] = True
                            q.append((r, c))
                cur = count2d(seen) - count2d(start_seen)
                if cur > best:
                    best = cur
                    best_pos = (sr, sc)
                    best_seen = copy2d(seen)
        return best, best_pos, best_seen

    start_seen = [[False for _ in range(cols)] for _ in range(rows)]
    ans = 0
    for i in range(3):
        best, best_pos, best_seen = find_best(start_seen)
        ans += best
        start_seen = copy2d(best_seen)
    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
