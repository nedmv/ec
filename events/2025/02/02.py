class Num:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def mul(self, other):
        a = self.x * other.x - self.y * other.y
        b = self.x * other.y + self.y * other.x
        self.x, self.y = a, b

    def div(self, other):
        self.x, self.y = int(self.x / other.x), int(self.y / other.y)

    def show(self):
        return f"[{self.x},{self.y}]"

    def check(self):
        return (-1000000 <= self.x <= 1000000) and (-1000000 <= self.y <= 1000000)


def get_xy(D):
    x = int(D[0].split("[")[1].split(",")[0])
    y = int(D[0].split("[")[1].split(",")[1].split("]")[0])
    return x, y


def part1(D):
    x, y = get_xy(D)
    A = Num(x, y)
    ans = Num()

    for i in range(3):
        ans.mul(ans)
        ans.div(Num(10, 10))
        ans.add(A)

    return ans.show()


def solve(D, step):
    x, y = get_xy(D)

    def examine(p):
        ans = Num()
        for _ in range(100):
            ans.mul(ans)
            ans.div(Num(100000, 100000))
            ans.add(p)
            if not ans.check():
                return False
        return True

    ans = 0
    for r in range(x, x + 1001, step):
        for c in range(y, y + 1001, step):
            if examine(Num(r, c)):
                ans += 1

    return ans


def part2(D):
    return solve(D, 10)


def part3(D):
    return solve(D, 1)


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
