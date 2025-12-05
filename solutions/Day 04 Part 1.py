import aoc
contents = aoc.get_input(2025, 4).strip()
del aoc

# ---

lines = contents.split("\n")

def adj(y, x):
    r = 0
    for p in {
        (y-1, x-1),
        (y, x-1),
        (y+1, x-1),
        (y-1, x),
        (y+1, x),
        (y-1, x+1),
        (y, x+1),
        (y+1, x+1)
    }:
        if not (0 <= p[0] < len(lines)) or not (0 <= p[1] < len(lines[0])):
            continue
        r += (lines[p[0]][p[1]] == "@")
    return r < 4

s = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "@" and adj(y, x):
            s += 1


print(s)