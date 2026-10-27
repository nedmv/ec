def solve(D, generator):
    gen = generator()
    target = next(gen)
    ans = 0
    for s in D[0].split(','):
        num = int(s)
        while True:
            if target >= num:
                ans += target - num
                break
            # input is increasing sequence
            target = next(gen)
    return ans

def part1(D):
    def generator1():
        i = 1
        while True:
            yield i**2
            i += 1
    return solve(D, generator1)

def part2(D):
    def generator2():
        i = 2
        while True:
            yield 4*(i-1)
            i += 1
    return solve(D, generator2)

def part3(D):
    def generator3():
        i = 3
        while True:
            yield i**2 - 1
            i += 2
    return solve(D, generator3)

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)