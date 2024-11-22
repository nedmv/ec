import queue


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def dijkstra(self):
        rows = len(self.data)
        cols = len(self.data[0])

        m = [[self.data[row][col] for col in range(cols)] for row in range(rows)]

        end = (0, 0)
        starts = []

        for row in range(rows):
            for col in range(cols):
                if m[row][col] == "S":
                    m[row][col] = "0"
                    starts.append((row, col))
                elif m[row][col] == "E":
                    m[row][col] = "0"
                    end = (row, col)

        pq = queue.PriorityQueue()
        times = [[1e6 for col in range(cols)] for row in range(rows)]
        for start in starts:
            pq.put((0, start))
            times[start[0]][start[1]] = 0

        while pq:
            time, (row, col) = pq.get()
            if (row, col) == end:
                return time
            if time > times[row][col]:
                continue
            for r, c in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]:
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and m[r][c] != "#"
                    and m[r][c] != " "
                ):
                    diff = abs(ord(m[r][c]) - ord(m[row][col]))
                    next_time = time + min(diff, 10 - diff) + 1
                    if next_time < times[r][c]:
                        times[r][c] = next_time
                        pq.put(
                            (
                                next_time,
                                (r, c),
                            )
                        )
        return "No path found"

    def solve(self):
        print(self.dijkstra())


class Part1(Solver):
    input_path = "input1.txt"
    # input_path = "test1.txt"


class Part2(Solver):
    input_path = "input2.txt"


class Part3(Solver):
    input_path = "input3.txt"


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
