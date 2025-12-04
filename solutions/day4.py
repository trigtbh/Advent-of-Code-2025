import aoc
day = 4
contents = aoc.get_input(2025, day).strip()
del aoc

# ---
# part 1

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




print(f"Day {day} Part 1: {s}")


# ---
# part 2

lines = [[c for c in line] for line in contents.split("\n")]



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

print(f"Day {day} Part 2: {s2}")