from collections import deque
from queue import PriorityQueue


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        time_limit = 100
        alt = 1000

        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        start = (0, 0)
        for row in range(len(m)):
            for col in range(len(m[0])):
                if m[row][col] == "S":
                    start = (row, col)
                    break

        moves = (1, 0, -1, 0, 1)

        q = deque()
        for i in range(4):
            q.append((0, 1000, i, start))  # time, direction, pos

        targets = set()
        for row in range(len(m) - 1):
            for col in range(len(m[0]) - 1):
                if (
                    m[row][col] == "+"
                    and m[row + 1][col] == "+"
                    and m[row][col + 1] == "+"
                    and m[row + 1][col + 1] == "+"
                ):
                    targets.add((row, col))

        d = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]

        max_ans = 0
        while q:
            time, alt, direction, (row, col) = q.popleft()
            if time >= time_limit:
                continue
            if (row, col) in targets:
                max_ans = max(max_ans, alt + time_limit - time)
                continue

            for i in range(4):
                if i == (direction + 2) % 4:
                    continue
                r = row + moves[i]
                c = col + moves[i + 1]
                if 0 <= r < len(m) and 0 <= c < len(m[0]) and m[r][c] != "#":
                    new_alt = alt
                    if m[r][c] == ".":
                        new_alt -= 1
                    elif m[r][c] == "+":
                        new_alt += 1
                    elif m[r][c] == "-":
                        new_alt -= 2
                    if d[r][c] < new_alt:
                        q.append((time + 1, new_alt, i, (r, c)))
                        d[r][c] = new_alt

        print(max_ans)


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        start_alt = 10000

        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        start = (0, 0)
        for row in range(len(m)):
            for col in range(len(m[0])):
                if m[row][col] == "S":
                    start = (row, col)
                    break

        moves = (1, 0, -1, 0, 1)

        pq = PriorityQueue()
        for i in range(4):
            pq.put((0, start_alt, i, start, 0))  # time, alt direction, pos, target
        targets = [(0, 0), (0, 0), (0, 0)]
        for row in range(len(m) - 1):
            for col in range(len(m[0]) - 1):
                if m[row][col] == "A":
                    targets[0] = (row, col)
                elif m[row][col] == "B":
                    targets[1] = (row, col)
                elif m[row][col] == "C":
                    targets[2] = (row, col)
        targets.append(start)

        d = [
            [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
            for _ in range(len(targets))
        ]

        while pq:
            time, alt, direction, (row, col), target = pq.get()
            if (row, col) == targets[target]:
                if target == 3 and alt >= start_alt:
                    print(time)
                    break
                target += 1

            for i in range(4):
                if i == (direction + 2) % 4:
                    continue
                r = row + moves[i]
                c = col + moves[i + 1]
                if 0 <= r < len(m) and 0 <= c < len(m[0]) and m[r][c] != "#":
                    new_alt = alt
                    if m[r][c] == "+":
                        new_alt += 1
                    elif m[r][c] == "-":
                        new_alt -= 2
                    else:
                        new_alt -= 1
                    if d[target][r][c] < new_alt and new_alt < 10500:
                        pq.put((time + 1, new_alt, i, (r, c), target))
                        d[target][r][c] = new_alt


class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]
        start_alt = 384400
        start_col = m[0].index("S")

        targets = []
        for col in range(len(m[0])):
            pick = False
            for row in range(len(m)):
                match m[row][col]:
                    case "+":
                        pick = True
                    case ".":
                        pass
                    case _:
                        pick = False
                        break
            if pick:
                targets.append(col)

        min_diff = 10000
        min_depth = 0
        for t in targets:
            depth = 0
            for row in range(len(m)):
                if m[row][t] == "+":
                    depth = row
                    break
            diff = abs(t - start_col) + depth - 1
            if diff < min_diff:
                min_diff = diff
                min_depth = depth

        alt = start_alt - min_diff

        # print(min_depth, min_diff)

        loops = alt // 4
        rem = alt % 4
        ans = loops * 8 + min_depth - 1
        match rem:
            case 1:
                ans += 3
            case 2:
                ans += 4
            case 3:
                ans += 7
        print(ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
