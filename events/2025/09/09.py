def similarity(a, b, c):
    n = len(a)
    p1 = 0
    p2 = 0
    for i in range(n):
        if c[i] != a[i] and c[i] != b[i]:
            return 0
        if c[i] == a[i]:
            p1 += 1
        if c[i] == b[i]:
            p2 += 1
    return p1 * p2


def part1(D):
    ans = 0
    A = D[0][2:]
    B = D[1][2:]
    C = D[2][2:]

    ans = similarity(A, B, C)
    if not ans:
        ans = similarity(A, C, B)
    if not ans:
        ans = similarity(B, C, A)
    return ans


def part2(D):
    ans = 0
    ducks = [x.split(":")[1] for x in D]
    t = len(ducks)

    for a in range(t - 2):
        A = ducks[a]
        for b in range(a + 1, t - 1):
            B = ducks[b]
            for c in range(b + 1, t):
                C = ducks[c]
                res = max(
                    0, similarity(A, B, C), similarity(B, C, A), similarity(C, A, B)
                )
                if res > 0:
                    ans += res

    return ans


def part3(D):
    ans = 0
    ducks = [x.split(":")[1] for x in D]
    t = len(ducks)

    size = [1 for _ in range(t)]
    parent = [x for x in range(t)]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def join(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        size[x] += size[y]
        parent[y] = x

    for a in range(t - 2):
        A = ducks[a]
        for b in range(a + 1, t - 1):
            B = ducks[b]
            for c in range(b + 1, t):
                C = ducks[c]
                res = max(
                    0, similarity(A, B, C), similarity(B, C, A), similarity(C, A, B)
                )
                if res > 0:
                    join(a, b)
                    join(a, c)
                    join(b, c)
    max_size = max(size)
    target = 0
    for i in range(t):
        if size[i] == max_size:
            target = i
            break
    for i in range(t):
        if find(i) == target:
            ans += i + 1
    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
