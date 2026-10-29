def solve(D):
    ans = 0
    for line in D:
        validate = line[3] == '2'
        standard, vote = line.split('-')[1].split()

        def num(ch):
            return ord(ch)-ord('0')
        def calc(a, b):
            n = len(b)
            m = len(a)
            res = 0
            for i in range(n):
                res += num(b[i]) * pow(num(a[m-1 - (n-1-i) % m]), n-1-i)
            return res

        cur = calc(standard, vote)
        ans += cur
        if validate:
            for i in reversed(range(cur, int(vote))):
                if calc(standard, str(i)) == cur:
                    ans -= cur
                    break

    return ans

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(solve, solve, solve)