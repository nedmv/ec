from collections import deque


class Solver:
    input_path = ""
    moves = (1, 0, -1, 0, 1)

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def init(self):
        self.m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]
        self.palms = []
        for row in range(len(self.m)):
            for col in range(len(self.m[0])):
                if self.m[row][col] == "P":
                    self.palms.append((row, col))

    def find_starts(self, find_all=False):
        starts = []

        if find_all:
            for row in range(len(self.m)):
                for col in range(len(self.m[0])):
                    if self.m[row][col] == ".":
                        starts.append((row, col))
        else:
            for row in range(len(self.m)):
                if self.m[row][0] == ".":
                    starts.append((row, 0))
                if self.m[row][-1] == ".":  # part 2
                    starts.append((row, len(self.m[0]) - 1))
        return starts

    # Returns (time, sum of times for all palms)
    def bfs(self, starts):
        palms = self.palms.copy()
        cnt = 0
        seen = set()
        q = deque()
        for s in starts:
            q.append((0, s))
            seen.add(s)
        while q:
            time, (row, col) = q.popleft()
            if (row, col) in palms:
                palms.remove((row, col))
                cnt += time
                if not palms:
                    break

            for i in range(4):
                r, c = row + self.moves[i], col + self.moves[i + 1]
                if (
                    0 <= r < len(self.m)
                    and 0 <= c < len(self.m[0])
                    and self.m[r][c] != "#"
                    and (r, c) not in seen
                ):
                    q.append((time + 1, (r, c)))
                    seen.add((r, c))

        return time, cnt


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        self.init()
        starts = self.find_starts()
        time, _ = self.bfs(starts)
        print(time)


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        self.init()
        starts = self.find_starts()
        time, _ = self.bfs(starts)
        print(time)


# brute force, just try every possible start
class Part3(Solver):
    input_path = "input3.txt"
    # input_path = "test3.txt"

    def solve(self):
        self.init()
        starts = self.find_starts(find_all=True)

        min_sum = 1e6
        cnt = 0
        for start in starts:
            cnt += 1
            if cnt % 100 == 0:
                print(f"Processed {cnt} start points")
            _, cur_sum = self.bfs([start])
            min_sum = min(min_sum, cur_sum)

        print(min_sum)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
