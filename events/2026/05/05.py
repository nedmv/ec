def init_map(data):
    m = [[ch for ch in data[i]] for i in range(len(data))]
    rows, cols = len(m), len(m[0])
    m[rows // 2][cols // 2] = '#'
    return m

def calc_elements(m, target):
    rows, cols = len(m), len(m[0])
    cnt = 0
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == target:
                cnt += 1
    return cnt

def transform(m, condition, target, limit=1_000_000):
    rows, cols = len(m), len(m[0])
    neighbors = []
    for r in range(rows):
        for c in range(cols):
            neighbors.append((r, c))

    for _ in range(limit):
        q = []
        for row, col in neighbors:
            if condition(m, row, col):
                q.append((row, col))
        if not q:
            break
        neighbors = set()
        for row, col in q:
            m[row][col] = target
            for r in (row-1, row, row+1):
                if 0 > r or r >= rows:
                    continue
                for c in (col-1, col, col+1):
                    if 0 > c or c >= cols or (r == row and c == col):
                        continue
                    neighbors.add((r, c))

def check_land(m, row, col):
    rows, cols = len(m), len(m[0])
    if m[row][col] == '#':
        return False
    cnt = 0
    has_land_neighbor = False
    for r in (row-1, row, row+1):
        if r < 0 or r >= rows:
            continue
        for c in (col-1, col, col+1):
            if c < 0 or c >= cols or (r == row and c == col):
                continue
            if m[r][c] == '#':
                has_land_neighbor = True
            cnt += m[r][c] in ('#', '1')
    return has_land_neighbor and cnt >= 5

def is_not_land(m, row, col):
    return m[row][col] != '#'

def check_sand(m, row, col):
    rows, cols = len(m), len(m[0])
    if m[row][col] in ('.', '='):
        return False
    cnt = 0
    for r in (row-1, row, row+1):
        if r < 0 or r >= rows:
            return True
        for c in (col-1, col, col+1):
            if c < 0 or c >= cols or m[r][c] == '.':
                return True
            cnt += m[r][c] == '='
    return cnt >= 5

def check_tree(m, row, col):
    rows, cols = len(m), len(m[0])
    if m[row][col] != '#':
        return False
    for i in (-2, -1, 0, 1, 2):
        r = row + i
        if r < 0 or r >= rows:
            return False
        for j in (-2, -1, 0, 1, 2):
            c = col + j
            if c < 0 or c >= cols:
                return False
            if i == j == 0 or (abs(i) == 2 and abs(j) == 2):
                continue
            if m[r][c] not in ('@', '#'):
                return False
    return True

def check_tree_2(m, row, col):
    if m[row][col] != '#':
        return False
    trees = 0
    for r in (row-1, row, row+1):
        for c in (col-1, col, col+1):
            if r == row and c == col:
                continue
            if m[r][c] == '=':
                return False
            if m[r][c] == '@':
                trees += 1
    return trees >= 4

def part1(D):
    m = init_map(D)

    transform(m, check_land, '#')

    return calc_elements(m, '#')

def part2(D):
    m = init_map(D)

    transform(m, check_land, '#')
    transform(m, is_not_land, '.', 1)
    transform(m, check_sand, '=')

    return calc_elements(m, '=')

def part3(D):
    m = init_map(D)

    transform(m, check_land, '#')
    transform(m, is_not_land, '.', 1)
    transform(m, check_sand, '=')
    transform(m, check_tree, '@')
    transform(m, check_tree_2, '@', 2)

    return calc_elements(m, '@')

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../../scripts")
    from ec import run

    run(part1, part2, part3)
