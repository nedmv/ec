class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        blocks = int(self.data[0])

        layer = -1
        s = 0
        while s < blocks:
            layer += 2
            s += layer
        ans = (s - blocks) * layer
        print(ans)


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        blocks = 20240000
        priests = int(self.data[0])
        acolytes = 1111

        # Test values
        # priests = 3
        # acolytes = 5
        # blocks = 50

        thickness = 1
        s = 1
        layers = 1
        while s < blocks:
            thickness *= priests
            thickness %= acolytes
            layers += 1
            s += thickness * (2 * layers - 1)
        ans = (s - blocks) * (2 * layers - 1)
        print(ans)


# a bit slow
class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        blocks = 202400000
        priests = int(self.data[0])
        acolytes = 10

        # Test values
        # priests = 2
        # acolytes = 5
        # blocks = 160

        thickness = 1
        s = 1
        layers = 1
        columns = [1]
        empty = 0
        while sum(columns) - empty < blocks:
            thickness *= priests
            thickness %= acolytes
            thickness += acolytes
            empty = 0
            for i in range(len(columns)):
                columns[i] += thickness
                empty += ((len(columns) + 2) * priests * columns[i]) % acolytes
            columns.insert(0, thickness)
            columns.append(thickness)
        ans = sum(columns) - empty - blocks
        print(ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
