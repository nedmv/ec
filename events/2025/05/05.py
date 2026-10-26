def get_data(data):
    id = int(data.split(":")[0])
    lst = data.split(":")[1]
    nums = [int(x) for x in lst.split(",")]

    segments = [[None, nums[0], None]]
    for num in nums[1:]:
        found = False
        for i in range(len(segments)):
            if num < segments[i][1] and not segments[i][0]:
                segments[i][0] = num
                found = True
                break
            elif num > segments[i][1] and not segments[i][2]:
                segments[i][2] = num
                found = True
                break
        if not found:
            segments.append([None, num, None])

    quality = int("".join([str(s[1]) for s in segments]))
    seg = []
    for s in segments:
        joined = ""
        for i in range(3):
            if s[i] is not None:
                joined += str(s[i])
        seg.append(int(joined))
    return quality, seg, id


def part1(D):
    quality, _, _ = get_data(D[0])
    return quality


def part2(D):
    l = float("inf")
    r = -float("inf")
    for data in D:
        q, _, _ = get_data(data)
        l = min(l, q)
        r = max(r, q)
    return r - l


def part3(D):
    swords = []
    for data in D:
        swords.append(get_data(data))
    swords.sort(reverse=True)

    ans = 0
    for i in range(len(swords)):
        ans += (i + 1) * swords[i][2]
    return ans


if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
