from collections import deque
from queue import PriorityQueue


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def bfs(self, m, start, end):
        rows = len(m)
        cols = len(m[0])

        q = deque()
        q.append((0, start))

        seen = set()
        seen.add(start)
        while q:
            time, (row, col) = q.popleft()
            if (row, col) == end:
                return time
            for r, c in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and m[r][c] != "#"
                    and (r, c) not in seen
                ):
                    q.append((time + 1, (r, c)))
                    seen.add((r, c))
        return 1e6


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        rows = len(self.data)
        cols = len(self.data[0])
        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        start = (0, 0)
        for i in range(cols):
            if m[0][i] == ".":
                start = (0, i)
        q = deque()
        q.append((0, start))
        m[start[0]][start[1]] = "#"

        ans = 0
        seen = set()
        while q:
            time, (row, col) = q.popleft()
            if m[row][col] == "H":
                ans = 2 * time
                break
            for r, c in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and m[r][c] != "#"
                    and (r, c) not in seen
                ):
                    q.append((time + 1, (r, c)))
                    seen.add((r, c))

        print(ans)


class Point:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.neighbors = []

    def add_neighbor(self, p, dist):
        self.neighbors.append((p, dist))


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        rows = len(self.data)
        cols = len(self.data[0])
        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        start = (0, 0)
        for i in range(cols):
            if m[0][i] == ".":
                start = (0, i)
                break

        types = ["A", "B", "C", "D", "E"]

        points = [Point(start[0], start[1], "S")]

        for row in range(rows):
            for col in range(cols):
                for t in range(len(types)):
                    if m[row][col] == types[t]:
                        points.append(Point(row, col, types[t]))
                        break

        dist = [[0 for _ in range(len(points))] for _ in range(len(points))]

        for s in range(len(points)):
            for f in range(s + 1, len(points)):
                if points[s].type == points[f].type:
                    continue
                d = self.bfs(m, (points[s].x, points[s].y), (points[f].x, points[f].y))
                dist[s][f] = d
                dist[f][s] = d

        # print("dist calculated")
        pq = PriorityQueue()
        pq.put((0, 0, "S", []))  # time, id, type, gathered

        times = [[1e6 for col in range(cols)] for row in range(rows)]

        while pq:
            time, id, type, gathered = pq.get()

            if len(gathered) == len(types):
                if id == 0:
                    print(time)
                    return
                pq.put((time + dist[0][id], 0, "S", gathered))
                # print(time + dist[0][id])

            for i in range(1, len(points)):
                if points[i].type in gathered:
                    continue
                pq.put(
                    (time + dist[id][i], i, points[i].type, gathered + [points[i].type])
                )

        # print(-1)


class Part3(Solver):
    input_path = "input3.txt"

    def find_start(self, m, letter):
        for row in range(len(m)):
            for col in range(len(m[0])):
                if m[row][col] == letter:
                    return (row, col)

    def partial_solve(self, m, letter, types):
        # print(letter, types)
        rows = len(self.data)
        cols = len(self.data[0])
        start = self.find_start(m, letter)
        points = [Point(start[0], start[1], letter)]

        for row in range(rows):
            for col in range(cols):
                for t in range(len(types)):
                    if m[row][col] == types[t]:
                        points.append(Point(row, col, types[t]))
                        break

        dist = [[0 for _ in range(len(points))] for _ in range(len(points))]

        for s in range(len(points)):
            for f in range(s + 1, len(points)):
                if points[s].type == points[f].type:
                    continue
                d = self.bfs(m, (points[s].x, points[s].y), (points[f].x, points[f].y))
                dist[s][f] = d
                dist[f][s] = d

        # print("dist calculated")
        pq = PriorityQueue()
        pq.put((0, 0, letter, []))  # time, id, type, gathered

        times = [[1e6 for col in range(cols)] for row in range(rows)]

        ans = 1e6
        while pq:
            time, id, type, gathered = pq.get()

            if len(gathered) == len(types):
                if id == 0:
                    # print(time)
                    return time
                pq.put((time + dist[0][id], 0, letter, gathered))
                if time + dist[0][id] < ans:
                    ans = time + dist[0][id]
                    # print(ans)
                    # print(time + dist[0][id])

            for i in range(1, len(points)):
                if points[i].type in gathered:
                    continue
                pq.put(
                    (time + dist[id][i], i, points[i].type, gathered + [points[i].type])
                )

        return 1e6

    def prepare_map(self): # Simplify the map based on guaranteed input properties
        rows = len(self.data)
        cols = len(self.data[0])
        m = [
            [self.data[row][col] for col in range(cols)]
            for row in range(rows)
        ]
        for i in range(cols):
            if m[0][i] == ".":
                m[0][i] = "S"
                break

        for i in range(cols):
            if m[rows - 2][i] == "E":
                m[rows - 2][i] = "."
                break

        for i in reversed(range(cols)):
            if m[rows - 2][i] == "R":
                m[rows - 2][i] = "."
                break

        for i in range(cols):
            if m[rows - 2][i] == "K":
                m[rows - 2][i] = "."

        return m

    def solve(self):
        m = self.prepare_map()
        ans = self.partial_solve(m, "S", ["E", "G", "H", "I", "J", "R"])
        ans += self.partial_solve(m, "E", ["A", "B", "C", "D"])
        ans += self.partial_solve(m, "R", ["N", "O", "P", "Q"])
        print(ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
