import aoc
contents = aoc.get_input(2025, 4).strip()
del aoc

# ---

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


lines = [[c for c in line] for line in contents.split("\n")]
s2 = 0
while True:
    r = 0
    points = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@" and adj(y, x):
                lines[y][x] = "."
                r += 1

            
    if r == 0: break
    s2 += r


print(s2)

