from collections import Counter


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")


class Part1(Solver):
    input_path = "input1.txt"
    # input_path = "test1.txt"

    def clap(self, clappers, times):
        for t in range(times):
            start = clappers[t % len(clappers)].pop(0)
            col = (t + 1) % len(clappers)

            n = len(clappers[col])
            pos = (start - 1) % (2 * n)
            if pos >= n:
                pos = 2 * n - pos
            clappers[col].insert(pos, start)

        return "".join([str(clappers[i][0]) for i in range(len(clappers))])

    def solve(self):
        clappers = [[int(x) for x in row.split(" ")] for row in self.data]

        clappers = [
            [clappers[row][col] for row in range(len(clappers))]
            for col in range(len(clappers[0]))
        ]
        print(self.clap(clappers, 10))


# a bit slow
class Part2(Solver):
    input_path = "input2.txt"
    # input_path = "test2.txt"

    def solve(self):
        clappers = [[int(x) for x in row.split(" ")] for row in self.data]

        clappers = [
            [clappers[row][col] for row in range(len(clappers))]
            for col in range(len(clappers[0]))
        ]

        cnt = Counter()
        t = 0
        while True:
            start = clappers[t % len(clappers)].pop(0)
            col = (t + 1) % len(clappers)

            n = len(clappers[col])
            pos = (start - 1) % (2 * n)
            if pos >= n:
                pos = 2 * n - pos
            clappers[col].insert(pos, start)
            shout = "".join([str(clappers[i][0]) for i in range(len(clappers))])
            cnt[shout] += 1
            if cnt[shout] == 2024:
                break
            t += 1

        print((t + 1) * int(shout))


class Part3(Solver):
    input_path = "input3.txt"
    # input_path = "test3.txt"

    def solve(self):
        clappers = [[int(x) for x in row.split(" ")] for row in self.data]

        clappers = [
            [clappers[row][col] for row in range(len(clappers))]
            for col in range(len(clappers[0]))
        ]

        t = 0
        highest = 0

        # non-generic solution, one should probably check repeats of whole pattern
        # originally i used much higher counter, but this proved to be enough for my input
        while t < 1000:
            start = clappers[t % len(clappers)].pop(0)
            col = (t + 1) % len(clappers)

            n = len(clappers[col])
            pos = (start - 1) % (2 * n)
            if pos >= n:
                pos = 2 * n - pos
            clappers[col].insert(pos, start)

            shout = "".join([str(clappers[i][0]) for i in range(len(clappers))])
            shout = int(shout)
            if shout > highest:
                highest = shout
            t += 1
        print(highest)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
