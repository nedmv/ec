import itertools
from multiprocessing import Pool
from sympy.utilities.iterables import multiset_permutations

class Solver:
  input_path = ""
  def __init__(self):
    with open(self.input_path) as f:
      self.data = f.read().split("\n")

  # p2, p3
  def load_track(self):
    track = []
    with open(self.racetrack) as f:
      track = f.read().split("\n")

    seen = set()
    seen.add((0, 0)) # must be last
    cur = (0, 1)
    self.track = []

    moves = (1, 0, -1, 0, 1)
    while cur not in seen:
      seen.add(cur)
      self.track.append(track[cur[0]][cur[1]])
      for i in range(4):
        next = (cur[0] + moves[i], cur[1] + moves[i+1])
        if next[0] < 0 or next[0] >= len(track) or next[1] < 0 or next[1] >= len(track[next[0]]) or next in seen or track[next[0]][next[1]] == " ":
          continue
        cur = next
        break
    self.track.append('S')
    # print(self.track)
  
  # p2, p3
  def get_plan_count(self, actions):
    power = 10
    total = 0
    for i in range(self.limit):
      action = actions[i % len(actions)]
      pos = self.track[i % len(self.track)]
      match pos:
        case '+':
          power += 1
        case '-':
          if power > 0:
            power -= 1
        case _:
          match action:
            case '+':
              power += 1
            case '-':
              if power > 0:
                power -= 1
            case _:
              pass
      total += power
    return total

class Part1(Solver):
  input_path = "input1.txt"
  def solve(self):
    squires = []
    for line in self.data:
      name = line.split(":")[0]
      actions = line.split(":")[1].split(",")
      power = 10
      total = 0
      for action in actions:
        if action == "=":
          pass
        elif action == "+":
          power += 1
        elif action == "-":
          if power > 0:
            power -= 1
        total += power
      squires.append((name, total))
    squires.sort(key=lambda x: x[1])
    ans = []
    for s in squires[::-1]:
      ans.append(s[0])

    print("".join(ans))

class Part2(Solver):
  input_path = "input2.txt"
  racetrack = "racetrack2.txt"
 
  def solve(self):
    squires = []
    self.load_track()
    self.limit = 10 * len(self.track)
    for line in self.data:
      name = line.split(":")[0]
      actions = line.split(":")[1].split(",")
      total = self.get_plan_count(actions)
      squires.append((name, total))
    squires.sort(key=lambda x: x[1])
    ans = []
    for s in squires[::-1]:
      ans.append(s[0])

    print("".join(ans))

class Part3(Solver):
  input_path = "input3.txt"
  racetrack = "racetrack3.txt"

  def solve(self):
    self.load_track()
    self.limit = 11 * len(self.track) # 2024 % 11 == 0
    rival_actions = self.data[0].split(":")[1].split(",")
    rival = self.get_plan_count(rival_actions)

    winning = 0
    for perm in multiset_permutations("".join(rival_actions)):
      if self.get_plan_count("".join(perm)) > rival:
        winning += 1
    print(winning)

def main():
  Part1().solve()
  Part2().solve()
  Part3().solve()

if __name__ == "__main__":
  main()