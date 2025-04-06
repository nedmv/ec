from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
import numpy as np
from scipy.spatial import Delaunay


class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    def solve1(self):
        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        rows = len(m)
        cols = len(m[0])

        stars = []

        for row in range(rows):
            for col in range(cols):
                if m[row][col] == "*":
                    stars.append((row, col))

        ans = len(stars)
        max_dist = 0
        connected = set()
        for star in stars:
            min_dist = 1e6
            for s in stars:
                if s != star:
                    min_dist = min(min_dist, abs(star[0] - s[0]) + abs(star[1] - s[1]))
            max_dist = max(min_dist, max_dist)
            ans += min_dist
        ans -= max_dist

        points = np.array(stars)
        tri = Delaunay(points)
        edges = tri.simplices
        ans = 0

        adj = csr_matrix((len(points), len(points)), dtype=int)
        for edge in edges:
            for pair in ((edge[0], edge[1]), (edge[0], edge[2]), (edge[1], edge[2])):
                if adj[pair[0], pair[1]] == 0:
                    dist = abs(points[pair[0]][0] - points[pair[1]][0]) + abs(
                        points[pair[0]][1] - points[pair[1]][1]
                    )
                    adj[pair[0], pair[1]] = dist
                    adj[pair[1], pair[0]] = dist

        ans = len(stars)
        mst = minimum_spanning_tree(adj).toarray().astype(int)
        for row in range(len(mst)):
            for col in range(len(mst)):
                if mst[row, col] != 0:
                    ans += mst[row, col]

        print(ans)


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        self.solve1()


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        self.solve1()


class Part3(Solver):
    input_path = "input3.txt"
    # input_path = "test3.txt"

    def solve(self):
        m = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        rows = len(m)
        cols = len(m[0])

        stars = []

        for row in range(rows):
            for col in range(cols):
                if m[row][col] == "*":
                    stars.append((row, col))

        ans = len(stars)
        max_dist = 0
        connected = set()
        for star in stars:
            min_dist = 1e6
            for s in stars:
                if s != star:
                    min_dist = min(min_dist, abs(star[0] - s[0]) + abs(star[1] - s[1]))
            max_dist = max(min_dist, max_dist)
            ans += min_dist
        ans -= max_dist

        points = np.array(stars)
        tri = Delaunay(points)
        edges = tri.simplices
        ans = 0

        adj = csr_matrix((len(points), len(points)), dtype=int)
        for edge in edges:
            for pair in ((edge[0], edge[1]), (edge[0], edge[2]), (edge[1], edge[2])):
                if adj[pair[0], pair[1]] == 0:
                    dist = abs(points[pair[0]][0] - points[pair[1]][0]) + abs(
                        points[pair[0]][1] - points[pair[1]][1]
                    )
                    if dist < 6:
                        adj[pair[0], pair[1]] = dist
                        adj[pair[1], pair[0]] = dist

        ans = len(stars)
        mst = minimum_spanning_tree(adj).toarray().astype(int)
        for row in range(len(mst)):
            for col in range(len(mst)):
                if mst[row, col] != 0:
                    ans += mst[row, col]
        n, comp = connected_components(mst)

        sizes = [0 for _ in range(n)]
        s = [set() for _ in range(n)]

        for row in range(len(mst)):
            for col in range(len(mst)):
                if mst[row, col] != 0:
                    sizes[comp[row]] += mst[row, col]
                    s[comp[row]].add(row)
                    s[comp[row]].add(col)

        for i in range(n):
            sizes[i] += len(s[i])

        sizes.sort()
        ans = 1
        for i in range(1, 4):
            ans *= sizes[-i]
        print(ans)


def main():
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
