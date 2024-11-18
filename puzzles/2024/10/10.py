class Solver:
    input_path = ""

    def __init__(self):
        with open(self.input_path) as f:
            self.data = f.read().split("\n")

    # p1, p2
    def get_runic(self, data):
        ans = []
        for i in range(2, 6):
            row = data[i][0] + data[i][1] + data[i][-2] + data[i][-1]
            for j in range(2, 6):
                col = data[0][j] + data[1][j] + data[-2][j] + data[-1][j]
                for k in col:
                    if k in row:
                        ans.append(k)
                        break
        return "".join(ans)

    # p2, p3
    @staticmethod
    def power(c):
        return ord(c) - ord("A") + 1

    @staticmethod
    def calc_power(runic):
        ans = 0
        for i in range(len(runic)):
            ans += Solver.power(runic[i]) * (i + 1)
        return ans


class Part1(Solver):
    input_path = "input1.txt"

    def solve(self):
        print(self.get_runic(self.data))


class Part2(Solver):
    input_path = "input2.txt"

    def solve(self):
        ans = 0
        for row in range(7):
            for col in range(15):
                data = self.extract(self.data, row * 9, col * 9)
                ans += self.calc_power(self.get_runic(data))
        print(ans)

    def extract(self, data, row, col):
        ans = []
        # row *= 9
        # col *= 9
        try:
            for i in range(row, row + 8):
                ans.append(data[i][col : col + 8])
        except IndexError:
            print(row, col)
        return ans


class Part3(Solver):
    input_path = "input3.txt"
    # input_path = "test3.txt"

    def update_runic(self, data, row, col):
        changed = False
        row_candidates = []
        col_candidates = []

        for r in range(row + 2, row + 6):
            try:
                row_candidates.append(
                    [data[r][col], data[r][col + 1], data[r][col + 6], data[r][col + 7]]
                )
            except IndexError:
                print(r, col, len(data), len(data[0]))
        for c in range(col + 2, col + 6):
            col_candidates.append(
                [data[row][c], data[row + 1][c], data[row + 6][c], data[row + 7][c]]
            )

        for r in range(row + 2, row + 6):
            rcand = row_candidates[r - (row + 2)]
            for c in range(col + 2, col + 6):
                ccand = col_candidates[c - (col + 2)]
                if data[r][c] == ".":
                    for rc in rcand:
                        if rc != "?" and rc in ccand:
                            data[r][c] = rc
                            rcand.remove(rc)
                            ccand.remove(rc)
                            changed = True
                            break
                else:
                    if data[r][c] in rcand:
                        rcand.remove(data[r][c])
                    if data[r][c] in ccand:
                        ccand.remove(data[r][c])
        for r in range(row + 2, row + 6):
            rcand = row_candidates[r - (row + 2)]
            if len(rcand) == 0:
                continue

            for c in range(col + 2, col + 6):
                if data[r][c] != ".":
                    continue

                ccand = col_candidates[c - (col + 2)]

                if len(rcand) == 1 and len(ccand) == 1:
                    if rcand[0] != ccand[0]:
                        if rcand[0] == "?":
                            data[r][c] = ccand[0]
                            if data[r][col] == "?":
                                data[r][col] = ccand[0]
                            elif data[r][col + 1] == "?":
                                data[r][col + 1] = ccand[0]
                            elif data[r][col + 6] == "?":
                                data[r][col + 6] = ccand[0]
                            elif data[r][col + 7] == "?":
                                data[r][col + 7] = ccand[0]
                            rcand.remove("?")
                            ccand.remove(ccand[0])
                            changed = True
                            break
                        elif ccand[0] == "?":
                            data[r][c] = rcand[0]

                            if data[row][c] == "?":
                                data[row][c] = rcand[0]
                            elif data[row + 1][c] == "?":
                                data[row + 1][c] = rcand[0]
                            elif data[row + 6][c] == "?":
                                data[row + 6][c] = rcand[0]
                            elif data[row + 7][c] == "?":
                                data[row + 7][c] = rcand[0]
                            break

                            rcand.remove(rcand[0])
                            ccand.remove("?")
                            changed = True
                            break
        return changed

    def get_runic(self, data, row, col):
        runic = []

        for r in range(row + 2, row + 6):
            for c in range(col + 2, col + 6):
                if data[r][c] == ".":
                    return ""
                runic.append(data[r][c])
        return "".join(runic)

    def write_mat(self, data):
        with open("mat3.txt", "w") as f:
            for row in range(len(data)):
                for col in range(len(data[0])):
                    f.write(data[row][col])
                f.write("\n")

    def solve(self):
        ans = 0

        data = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]

        updated = True
        count = 0
        while count < 10:
            count += 1
            updated = False
            for row in range(10):
                for col in range(20):
                    if self.update_runic(data, row * 6, col * 6):
                        updated = True

        # self.write_mat(data)

        for row in range(10):
            for col in range(20):
                runic = self.get_runic(data, row * 6, col * 6)
                if len(runic) > 0:
                    ans += self.calc_power(runic)
        print(ans)

    def test(self):
        ans = 0

        data = [
            [self.data[row][col] for col in range(len(self.data[0]))]
            for row in range(len(self.data))
        ]
        updated = True
        while updated:
            updated = False
            for row in range(2):
                for col in range(2):
                    if self.update_runic(data, row, col):
                        updated = True
        for row in range(2):
            for col in range(2):
                runic = self.get_runic(data, row, col)
                if len(runic) > 0:
                    ans += self.calc_power(runic)
        print(ans)


def main():
    assert Solver.calc_power("PTBVRCZHFLJWGMNS") == 1851
    Part1().solve()
    Part2().solve()
    Part3().solve()


if __name__ == "__main__":
    main()
