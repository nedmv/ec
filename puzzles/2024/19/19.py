class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def rotate(self, row, col, pos):
        neigh = []
        neigh = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col + 1),
            (row + 1, col + 1),
            (row + 1, col),
            (row + 1, col - 1),
            (row, col - 1),
        ]

        letters = []
        for r, c in neigh:
            letters.append(self.m[r][c])

        if self.pattern[pos] == "L":
            first = letters.pop(0)
            letters.append(first)
        else:
            last = letters.pop()
            letters.insert(0, last)

        for i in range(len(neigh)):
            r, c = neigh[i]
            self.m[r][c] = letters[i]

    def prepare(self):
        self.pattern = self.data[0]
        self.data = self.data[2:]
        self.m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

    def find_ans(self):
        search_end = False
        start = (0, 0)
        end = (0, 0)
        ans = []
        for row in range(len(self.m)):
            for col in range(len(self.m[0])):
                if self.m[row][col] == ">":
                    start = (row, col)
                    search_end = True
                elif self.m[row][col] == "<":
                    if search_end:
                        end = (row, col)
                        break
            if search_end:
                if end != (0, 0):
                    ans = self.m[row][start[1] + 1 : end[1]]
                break
        for i in range(len(ans)):
            if ord(ans[i]) < ord("0") or ord(ans[i]) > ord("9"):
                return
        return "".join(ans)

    def solve1(self, rounds):
        rows = len(self.m)
        cols = len(self.m[0])

        for i in range(rounds):
            pos = 0
            for row in range(1, rows - 1):
                for col in range(1, cols - 1):
                    self.rotate(row, col, pos)
                    pos = (pos + 1) % len(self.pattern)


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        self.prepare()
        self.solve1(1)
        ans = self.find_ans()
        print(ans)


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        self.prepare()
        self.solve1(100)
        ans = self.find_ans()
        print(ans)


# brute force till we have viable answer
class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        self.prepare()

        for i in range(1048576000):  # ~ 8200 iterations is enough
            self.solve1(1)
            ans = self.find_ans()
            if ans and len(ans) > 1:  # otherwise finds false ans with len 1
                print("Total iterations:", i)
                print(ans)
                break
            if i % 100 == 0:
                print(f"Passed {i} iterations")


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
