def solve(D, **kwargs):
    ans = 0
    n = kwargs['n']
    assert 1 <= n <= 9

    for line in D:
        next = [[] for _ in range(n)]
        prev = [0]*n
        for comp in line.split():
            a, b = int(comp[0])-1, int(comp[2])-1
            if comp[1] == '<':
                a, b = b, a
            next[a].append(b)
            prev[b] += 1

        ordered = []
        q = []
        for i in range(n):
            if prev[i] == 0:
                q.append(i)
        while q:
            a = q.pop()
            ordered.append(a+1)
            for i in next[a]:
                prev[i] -= 1
                if prev[i] == 0:
                    q.append(i)

        ans += int(''.join([str(i) for i in ordered]))
    return ans

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(solve, solve, solve,
        example={"1": {"n": 5}, "2": {"n": 5}, "3": {"n": 5}},
        input={"1": {"n": 5}, "2": {"n": 9}, "3": {"n": 9}})
