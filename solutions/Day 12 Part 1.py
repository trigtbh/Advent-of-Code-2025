import aoc
contents = aoc.get_input(2025, 12).strip()
del aoc

# ---

shapes = contents.split("\n\n")

regions = shapes[-1]
shapes = shapes[:-1]

sfinal = []
for s in shapes:
    lines = s.split("\n")[1:]
    f = 0
    for y in range(3):
        for x in range(3):
            if lines[y][x] == "#":
                f += 1
    sfinal.append(f)

ret = 0
rej = 0
for r in regions.split("\n"):
    area, usage = r.split(": ")
    usage = list(map(int, usage.split(" ")))
    avals = list(map(int, area.split("x")))
    a = avals[0] * avals[1]
    used = 0
    for i, item in enumerate(usage):
        used += sfinal[i] * item

    if used > a:
        rej += 1
        print("rejected:", r)

    else:
        ret += 1

print(ret)
print(rej)