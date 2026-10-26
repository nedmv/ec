class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def solve1(self, diagonal=False):
        m = [
            [1 if self.data[row][col] == "#" else 0 for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if diagonal:
            neighbors.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
        ans = 0
        has_diff = True
        level = 0
        while has_diff:
            has_diff = False
            level += 1
            for row in range(len(m)):
                for col in range(len(m[0])):
                    if m[row][col] == level:
                        for dr, dc in neighbors:
                            r, c = (row + dr, col + dc)
                            if (
                                r < 0
                                or r >= len(m)
                                or c < 0
                                or c >= len(m[0])
                                or m[r][c] < level
                            ):
                                break
                        else:
                            has_diff = True
                            m[row][col] = level + 1

        for row in range(len(m)):
            for col in range(len(m[0])):
                ans += m[row][col]
        print(ans)


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        self.solve1()


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        self.solve1()


class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        self.solve1(True)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
