class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def solve1(self):
        nails = []
        for i in self.data:
            nails.append(int(i))

        nails.sort()

        ans = 0
        for i in range(1, len(nails)):
            ans += nails[i] - nails[0]

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
        nails = []
        for i in self.data:
            nails.append(int(i))

        nails.sort()

        min_ans = 1e9
        for nail in nails:
            ans = 0
            for i in range(len(nails)):
                ans += abs(nails[i] - nail)
            min_ans = min(min_ans, ans)

        print(min_ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
