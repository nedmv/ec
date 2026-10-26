def parse(D):
    thickness = [1]
    incoming = [[]]
    testcases = []

    for line in D:
        if len(line) == 0:
            continue
        if line.startswith(('0', '1')):
            testcases.append([int(x) for x in line.split(" ")])
            continue

        thick = int(line.split(" ")[-1].split(":")[0])
        if line.startswith("Plant"):
            thickness.append(thick)
            incoming.append([])
        elif line.startswith("- free"):
            incoming[-1].append((0, thick))
        else:
            id = int(line.split(" ")[4])
            incoming[-1].append((id, thick))

    return thickness, incoming, testcases


def part1(D):
    thickness, incoming, _ = parse(D)
    n = len(thickness)
    energy = [0 for _ in range(n)]
    energy[0] = 1
    for i in range(1, n):
        for id, th in incoming[i]:
            energy[i] += energy[id] * th
        if energy[i] < thickness[i]:
            energy[i] = 0

    return energy[-1]


def part2(D):
    thickness, incoming, testcases = parse(D)
    n = len(thickness)
    n_test = len(testcases[0])
    ans = 0
    for t in testcases:
        energy = [0 for _ in range(n)]
        energy[0] = 1
        for i in range(1, n_test + 1):
            energy[i] = t[i - 1]
        for i in range(n_test + 1, n):
            for id, th in incoming[i]:
                energy[i] += energy[id] * th
            if energy[i] < thickness[i]:
                energy[i] = 0
        if energy[-1] > 0:
            ans += energy[-1]
    return ans


def part3(D):
    thickness, incoming, testcases = parse(D)
    n = len(thickness)
    n_test = len(testcases[0])

    thick_for_id = [[] for _ in range(n_test + 1)]

    for inc in incoming:
        for id, th in inc:
            if 0 < id <= n_test:
                thick_for_id[id].append(th)

    # This takes into account the property of real input: each starting plant
    # is connected to branches with positive or negative thickness only,
    # so we can easily determine best testcase.
    # For cases with min(thick) < 0 and max(thick) > 0,
    # like in testcase 3, we should try each variant.
    ideal = []
    for id in range(1, n_test + 1):
        for thick in thick_for_id:
            if len(thick) == 0:
                continue
            if min(thick) > 0:
                ideal.append(1)
            else:
                ideal.append(0)

    energy = [0 for _ in range(n)]
    energy[0] = 1
    for i in range(1, n_test + 1):
        energy[i] = ideal[i - 1]
    for i in range(n_test + 1, n):
        for id, th in incoming[i]:
            energy[i] += energy[id] * th
        if energy[i] < thickness[i]:
            energy[i] = 0
    max_energy = energy[-1]

    ans = 0
    for t in testcases:
        energy = [0 for _ in range(n)]
        energy[0] = 1
        for i in range(1, n_test + 1):
            energy[i] = t[i - 1]
        for i in range(n_test + 1, n):
            for id, th in incoming[i]:
                energy[i] += energy[id] * th
            if energy[i] < thickness[i]:
                energy[i] = 0
        if energy[-1] > 0:
            ans += max_energy - energy[-1]
    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
