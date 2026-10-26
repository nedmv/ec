import sys


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def find_distinct(self, root, path, paths):
        path.append(root)
        if root in self.fruits:
            for f in self.fruits[root]:
                if f == "@":
                    paths.append(path.copy())
                    continue
                elif f == "ANT" or f == "BUG":  # part 3
                    continue
                self.find_distinct(f, path, paths)
        path.pop()

    def solve1(self, full_words=False):
        self.fruits = {
            line.split(":")[0]: line.split(":")[1].split(",") for line in self.data
        }
        paths = []
        self.find_distinct("RR", [], paths)

        paths.sort(key=lambda x: len(x))
        ans = ""
        for i in range(len(paths)):
            if len(paths[i]) != len(paths[(i - 1) % len(paths)]) and len(
                paths[i]
            ) != len(paths[(i + 1) % len(paths)]):
                if full_words:
                    ans = "".join(paths[i]) + "@"
                else:
                    ans = "".join(x[0] for x in paths[i]) + "@"
                break
        print(ans)


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        self.solve1(full_words=True)


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        self.solve1()


class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        self.solve1()


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
