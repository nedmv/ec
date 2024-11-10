
class Solver:
  input_path = ""
  def __init__(self):
    with open(self.input_path) as f:
      self.data = f.read().split("\n")

  def parse_words(self, rtl=False):
    words1 = self.data[0].split(":")[1].split(",")
    words = words1.copy()
    if rtl:
      for w in words1:
        rev = w[::-1]
        if rev not in words:
          words.append(rev)
    return words

class Part1(Solver):
  input_path = "input1.txt"
  def solve(self):
    words = self.parse_words()
    line = self.data[2]

    ans = 0
    for w in words:
      start = 0
      while True:
        start = line.find(w, start)
        if start == -1:
          break
        ans += 1
        start += 1
    print(ans)

class Part2(Solver):
  input_path = "input2.txt"

  def solve(self):
    words = self.parse_words(True)

    ans = 0
    for id in range(2, len(self.data)):
      line = self.data[id]
      runic = [False] * len(line)
      for w in words:
        start = 0
        while True:
          start = line.find(w, start)
          if start == -1:
            break
          for i in range(start, start + len(w)):
            runic[i] = True
          start += 1
      ans += sum(runic)
    print(ans)

class Part3(Solver):
  input_path = "input3.txt"

  def solve(self):
    words = self.parse_words(True)
    words.sort(key=len, reverse=True)

    ans = 0
    rows = len(self.data)-2
    cols = len(self.data[2])
    grid = [[False for _ in range(cols)] for _ in range(rows)]

    # horizontal
    for row in range(rows):
      for col in range(cols):
        for w in words:
          found = True
          for i in range(len(w)):
            letter = self.data[row+2][(col+i)%cols]
            if letter != w[i]:
              found = False
              break
          if found:
            for i in range(len(w)):
              grid[row][(col+i)%cols] = True
            break # since words are sorted by length

    # vertical
    for col in range(cols):
      for row in range(rows):
        for w in words:
          if row + len(w) > rows: #do not wrap in vertical direction
            continue
          found = True
          for i in range(len(w)):
            letter = self.data[(row+i)%rows+2][col]
            if letter != w[i]:
              found = False
              break
          if found:
            for i in range(len(w)):
              grid[(row+i)%rows][col] = True
            break # since words are sorted by length
    ans = 0
    for row in range(rows):
      for col in range(cols):
        if grid[row][col]:
          ans += 1
    print(ans)

def main():
  Part1().solve()
  Part2().solve()
  Part3().solve()

if __name__ == "__main__":
  main()