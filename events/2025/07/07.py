def parse(D):
    names = D[0].split(",")
    rules = []
    for line in D[2:]:
        first = line.split(" ")[0]
        last = line.split(" ")[2].split(",")
        rules.append([first, last])
    return names, rules


def part1(D):
    names, rules = parse(D)
    ans = 0
    for name in names:
        success = True
        for i in range(len(name) - 1):
            for rule in rules:
                if name[i] == rule[0] and name[i + 1] not in rule[1]:
                    success = False
                    break
                if not success:
                    break
            if not success:
                break
        if success:
            ans = name
            break

    return ans


def part2(D):
    names, rules = parse(D)
    ans = 0
    pos = 1
    for name in names:
        success = True
        for i in range(len(name) - 1):
            for rule in rules:
                if name[i] == rule[0] and name[i + 1] not in rule[1]:
                    success = False
                    break
                if not success:
                    break
            if not success:
                break
        if success:
            ans += pos
        pos += 1

    return ans


def part3(D):
    names, rules = parse(D)
    ans = set()

    def rec(prefix):
        if len(prefix) >= 7:
            # if prefix not in ans:
            ans.add(prefix)
        if len(prefix) == 11:
            return
        for i, rule in enumerate(rules):
            if prefix[-1] == rule[0]:
                for l in rule[1]:
                    prefix += l
                    rec(prefix)
                    prefix = prefix[0 : len(prefix) - 1]

    for name in names:
        banned = False
        for i in range(len(name) - 1):
            for pos, rule in enumerate(rules):
                if name[i] == rule[0] and name[i + 1] not in rule[1]:
                    banned = True
                    break
        if not banned:
            rec(name)
    return len(ans)


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
