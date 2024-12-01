from math import lcm
from collections import Counter


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def parse(self):
        turns = self.data[0].split(",")
        for t in range(len(turns)):
            turns[t] = int(turns[t])
        faces = len(turns)
        wheels = [[] for _ in range(len(turns))]
        for row in range(2, len(self.data)):
            for w in range(len(wheels)):
                try:
                    if self.data[row][w * 4] != " ":
                        wheels[w].append(self.data[row][w * 4 : (w + 1) * 4 - 1])
                except IndexError:
                    break

        positions = [0 for _ in range(len(wheels))]
        return turns, wheels, positions

    def calc(self, pattern):
        c = Counter(pattern)
        cnt = 0
        for k, v in c.items():
            if v >= 3:
                cnt += v - 2
        return cnt


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        turns, wheels, positions = self.parse()
        for t in range(100):
            for i in range(len(wheels)):
                positions[i] = (positions[i] + turns[i]) % len(wheels[i])

        for w in range(len(wheels)):
            print(wheels[w][positions[w]], end=" ")
        print()


class Part2(Solver):
    input_path = "input2.txt"
    # input_path = "test2.txt"

    def solve(self):
        pulls = 202420242024
        turns, wheels, positions = self.parse()

        cycle_len = 0
        cycle_ans = 0
        tail_ans = 0

        seen = set()
        seen.add(tuple(positions))
        last_seen = {}
        last_seen[tuple(positions)] = 0
        tails = []

        for i in range(pulls):
            cur = []
            for w in range(len(wheels)):
                positions[w] = (positions[w] + turns[w]) % len(wheels[w])
                cur.append(wheels[w][positions[w]][0])
                cur.append(wheels[w][positions[w]][2])
            cycle_ans += self.calc(cur)
            if tuple(positions) in seen:
                cycle_len = i - last_seen[tuple(positions)] + 1
                break
            seen.add(tuple(positions))
            last_seen[tuple(positions)] = i
            tails.append(cycle_ans)

        total_cycles = pulls // cycle_len
        tail = pulls % cycle_len
        ans = cycle_ans * total_cycles + tails[tail]
        print(ans)


class Part3(Solver):
    input_path = "input3.txt"
    # input_path = "test3.txt"

    def rec(self, dp, pulls, turns, wheels, positions):
        if pulls <= 0:
            return (0, 0)
        if tuple(positions) in dp[pulls]:
            return dp[pulls][tuple(positions)]
        ans = (0, 1e10)
        for diff in (-1, 0, 1):
            poses = [0 for p in positions]
            for w in range(len(wheels)):
                poses[w] = (positions[w] + diff + turns[w]) % len(wheels[w])
            cur = []
            for w in range(len(wheels)):
                cur.append(wheels[w][poses[w]][0])
                cur.append(wheels[w][poses[w]][2])

            rec_ans = self.rec(dp, pulls - 1, turns, wheels, poses)
            calc_ans = self.calc(cur)
            ans = (
                max(ans[0], calc_ans + rec_ans[0]),
                min(ans[1], calc_ans + rec_ans[1]),
            )
        dp[pulls][tuple(positions)] = ans
        return ans

    def solve(self):
        pulls = 256
        turns, wheels, positions = self.parse()

        dp = [{} for _ in range(pulls + 1)]

        ans = self.rec(dp, pulls, turns, wheels, positions)
        print(ans[0], ans[1])


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
