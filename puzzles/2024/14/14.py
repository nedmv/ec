from collections import deque


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    # p2, p3
    def add(self, seen, pos, id, val):
        for i in range(val):
            pos[id] += 1
            seen.add((pos[0], pos[1], pos[2]))

    # p2, p3
    def sub(self, seen, pos, id, val):
        for i in range(val):
            pos[id] -= 1
            seen.add((pos[0], pos[1], pos[2]))

    # p2, p3
    def get_nodes_and_leaves(self):
        seen = set()
        leaves = []

        for line in self.data:
            pos = [0, 0, 0]
            for inst in line.split(","):
                dir = inst[0]
                num = int(inst[1:])
                match dir:
                    case "U":
                        self.add(seen, pos, 1, num)
                    case "D":
                        self.sub(seen, pos, 1, num)
                    case "L":
                        self.add(seen, pos, 0, num)
                    case "R":
                        self.sub(seen, pos, 0, num)
                    case "F":
                        self.add(seen, pos, 2, num)
                    case "B":
                        self.sub(seen, pos, 2, num)
            leaves.append((pos[0], pos[1], pos[2]))
        return seen, leaves


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        pos = [0, 0, 0]
        max_height = 0

        for inst in self.data[0].split(","):
            dir = inst[0]
            num = int(inst[1:])
            if dir == "U":
                pos[1] += num
                max_height = max(max_height, pos[1])
            elif dir == "D":
                pos[1] -= num
        print(max_height)


class Part2(Solver):
    input_path = "input2.txt"
    # input_path = "test2.txt"

    def solve(self):
        seen, _ = self.get_nodes_and_leaves()
        print(len(seen))


class Part3(Solver):
    input_path = "input3.txt"

    def solve(self):
        seen, leaves = self.get_nodes_and_leaves()

        trunk = []
        for pos in seen:
            if pos[0] == 0 and pos[2] == 0:
                trunk.append(pos)

        min_murk = 1e9
        for t in trunk:
            visited = set()
            cur_leaves = list(leaves)
            murk = 0
            q = deque()
            q.append((0, t))
            visited.add(t)
            while q:
                (d, p) = q.popleft()
                for l in cur_leaves:
                    if p == l:
                        murk += d
                        cur_leaves.remove(l)
                        break
                for x, y, z in [
                    (p[0] + 1, p[1], p[2]),
                    (p[0] - 1, p[1], p[2]),
                    (p[0], p[1] + 1, p[2]),
                    (p[0], p[1] - 1, p[2]),
                    (p[0], p[1], p[2] + 1),
                    (p[0], p[1], p[2] - 1),
                ]:
                    if (x, y, z) not in seen or (x, y, z) in visited:
                        continue
                    visited.add((x, y, z))
                    q.append(((d + 1), (x, y, z)))
            min_murk = min(min_murk, murk)

        print(min_murk)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
