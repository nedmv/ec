from collections import defaultdict
from math import inf


def part1(D):
    results = defaultdict(int)
    for line in D:
        id, _, _, time = (int(s.split('=')[1]) for s in line.split())
        results[id] += time
    times = list(results.values())
    times.sort()

    ans = 0
    place = 1
    for time in times:
        ans += time * place
        place += 1
    return ans


def part2(D):
    results = defaultdict(int)
    parts = defaultdict(int)
    for line in D:
        id, _, _, time = (int(s.split('=')[1]) for s in line.split())
        results[id] += time
        parts[id] += 1
    times = list(results.items())
    times.sort(key = lambda x: (-parts[x[0]], x[1]))

    ans = 0
    place = 1
    for _, time in times:
        ans += time * place
        place += 1
    return ans


def part3(D):
    ans = 0
    data = []
    for line in D:
        id, quest, part, time = (int(s.split('=')[1]) for s in line.split())
        data.append((id, quest, part, time))

    total_quests = max(data, key = lambda x: x[1])[1]
    total_ids = max(data, key = lambda x: x[0])[0]
    results = [[[inf for _ in range(3)] for _ in range(total_quests)] for _ in range(total_ids)]
    for id, quest, part, time in data:
        results[id-1][quest-1][part-1] = time

    for id in range(total_ids):
        for quest in range(total_quests):
            for part in range(1, 3):
                results[id][quest][part] += results[id][quest][part-1]

    scores = [0 for _ in range(total_ids)]
    for quest in range(total_quests):
        for part in range(3):
            part_times = []
            for id in range(total_ids):
                time = results[id][quest][part]
                if time != inf:
                    part_times.append((time, id))
            part_times.sort()
            last_time = 0
            last_score = 50 * (part+1)
            next_score = last_score
            for time, id in part_times:
                if last_time != time:
                    last_score = next_score
                last_time = time
                if last_score > 0:
                    scores[id] += last_score
                next_score -= 1

    scores.sort(reverse=True)
    last_score = inf
    last_place = 1
    next_place = 1
    for score in scores:
        if last_score != score:
            last_place = next_place
        last_score = score
        ans += last_place * last_score
        next_place += 1
    return ans

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)