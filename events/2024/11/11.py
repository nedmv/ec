class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")
    def calc(self, rules, starter, days):
        counts = {starter: 1}
        for i in range(days):
            next = {}

            for k, v in counts.items():
                for r in rules[k]:
                    if r not in next:
                        next[r] = v
                    else:
                        next[r] += v
            counts = next

        sum = 0
        for _, v in counts.items():
            sum += v
        return sum

class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        rules = {}
        for line in self.data:
            rules[line.split(":")[0]] = line.split(":")[1].split(",")

        print(self.calc(rules, 'A', 4))



class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        rules = {}
        for line in self.data:
            rules[line.split(":")[0]] = line.split(":")[1].split(",")

        print(self.calc(rules, 'Z', 10))

class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        rules = {}
        for line in self.data:
            rules[line.split(":")[0]] = line.split(":")[1].split(",")

        max_val = 0
        min_val = 1e40
        for name, _ in rules.items():
            sum = self.calc(rules, name, 20)
            max_val = max(max_val, sum)
            min_val = min(min_val, sum)
        ans = max_val - min_val

        print(ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
