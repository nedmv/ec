class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def cost(self, c):
        match (c):
            case "A":
                return 0
            case "B":
                return 1
            case "C":
                return 3
            case "D":
                return 5
            case _:
                return 0
        return 0


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        cnt = 0
        for c in self.data[0]:
            cnt += self.cost(c)
        print(cnt)


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        cnt = 0
        for i in range(0, len(self.data[0]), 2):
            a = self.data[0][i]
            b = self.data[0][i + 1]

            if a != "x" and b != "x":
                cnt += 2

            cnt += self.cost(a)
            cnt += self.cost(b)

        print(cnt)


class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        cnt = 0
        for i in range(0, len(self.data[0]), 3):
            a = self.data[0][i]
            b = self.data[0][i + 1]
            c = self.data[0][i + 2]

            x_count = 0
            if a == "x":
                x_count += 1
            if b == "x":
                x_count += 1
            if c == "x":
                x_count += 1
            if x_count == 0:
                cnt += 6
            elif x_count == 1:
                cnt += 2

            cnt += self.cost(a)
            cnt += self.cost(b)
            cnt += self.cost(c)
        print(cnt)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
