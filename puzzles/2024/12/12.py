class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def solve_p1_p2(self):
        targets = []
        for y in range(len(self.data)):
            line = self.data[-y - 1]
            for x in range(len(line)):
                if line[x] == "T":
                    targets.append((x, y, 1))
                elif line[x] == "H":
                    targets.append((x, y, 2))

        targets.sort(key=lambda x: (x[1], x[0]))

        cannons = [(1, 1), (1, 2), (1, 3)]

        ans = 0
        for t in targets:
            power = 0
            found = -1
            while found == -1:
                power += 1
                for cannon in range(3):
                    pos = cannons[cannon]
                    for _ in range(power):
                        pos = (pos[0] + 1, pos[1] + 1)
                        if pos[0] == t[0] and pos[1] == t[1]:
                            break
                    for _ in range(power):
                        pos = (pos[0] + 1, pos[1])
                        if pos[0] == t[0] and pos[1] == t[1]:
                            break
                    while pos[1] >= t[1]:
                        pos = (pos[0] + 1, pos[1] - 1)
                        if pos[0] == t[0] and pos[1] == t[1]:
                            break
                    if pos[0] == t[0] and pos[1] == t[1]:
                        found = cannon
                        break
            ans += power * (found + 1) * t[2]

        return ans


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        print(self.solve_p1_p2())


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        print(self.solve_p1_p2())


class Part3(Solver):
    input_path = "input3.txt"
    # input_path = "test3.txt"

    # messy and time-consuming brute force
    def solve(self):
        meteors = []
        for line in self.data:
            meteors.append((int(line.split(" ")[0]), int(line.split(" ")[1])))

        cannons = [(0, 0), (0, 1), (0, 2)]
        ans = 0

        i = 0
        for m in meteors:
            max_h = -1
            min_score = 1e6
            for cannon in range(3):
                cur_h = -1
                cur_score = 0
                for t in range(min(m[0], m[1]) + 1):
                    for power in range(1, (min(m[0], m[1]) + 1)):
                        pos = cannons[cannon]
                        ticks = 0
                        mpos = (m[0] - t, m[1] - t)
                        while (
                            (mpos[1] > -1)
                            and (pos[0] <= mpos[0])
                            and (pos[1] > -1)
                            and (ticks < 2 * power or pos[1] >= mpos[1])
                        ):
                            if ticks < power:
                                pos = (pos[0] + 1, pos[1] + 1)
                            elif ticks < 2 * power:
                                pos = (pos[0] + 1, pos[1])
                            else:
                                pos = (pos[0] + 1, pos[1] - 1)
                            mpos = (mpos[0] - 1, mpos[1] - 1)
                            if pos[0] == mpos[0] and pos[1] == mpos[1]:
                                cur_h = mpos[1]
                                cur_score = (cannon + 1) * power
                                break
                            ticks += 1

                        if cur_score > 0:
                            break
                    if cur_score > 0:
                        break
                if cur_h > max_h:
                    max_h = cur_h
                    min_score = cur_score
                elif cur_h == max_h:
                    min_score = min(min_score, cur_score)
            # print(i, min_score)
            i += 1
            ans += min_score

        print(ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
