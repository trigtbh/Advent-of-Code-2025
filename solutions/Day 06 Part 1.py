import aoc
contents = aoc.get_input(2025, 6).strip()
del aoc

# ---

lines = contents.split("\n")
grid = [[x for x in l.split(" ") if x] for l in lines]

ret = 0
for x in range(len(grid[0])):
    op = grid[-1][x]
    s = 0
    if op == "+":
        for i in range(len(grid) - 1):
            s += int(grid[i][x])
    else:
        s = 1
        for i in range(len(grid) - 1):
            s *= int(grid[i][x])
    ret += s

print(ret)