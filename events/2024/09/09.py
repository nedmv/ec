class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def count(self, stamps, callback=None):
        cnt = 0
        data = [int(e) for e in self.data]
        max_val = max(data)

        dp = [max_val for _ in range(max_val + 1)]
        dp[0] = 0
        for i in range(1, max_val + 1):
            for s in stamps:
                if i - s >= 0:
                    dp[i] = min(dp[i], dp[i - s] + 1)
        for e in data:
            if callback:
                cnt += callback(dp, e)
            else:
                cnt += dp[e]
        return cnt


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        stamps = (10, 5, 3, 1)
        print(self.count(stamps))


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        stamps = (30, 25, 24, 20, 16, 15, 10, 5, 3, 1)
        print(self.count(stamps))


class Part3(Solver):
    input_path = "input3.txt"

    def callback(self, dp, e):
        best = e
        for i in range(0, 51 if e % 2 == 0 else 50):
            l = e // 2 - i
            r = (e + 1) // 2 + i
            best = min(best, dp[l] + dp[r])
        return best

    def solve(self):
        stamps = (101, 100, 75, 74, 50, 49, 38, 37, 30, 25, 24, 20, 16, 15, 10, 5, 3, 1)
        print(self.count(stamps, self.callback))


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
