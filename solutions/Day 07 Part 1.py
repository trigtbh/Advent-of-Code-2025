import aoc
contents = aoc.get_input(2025, 7).strip()
del aoc

# ---

lines = contents.split("\n")
start = lines[0].index("S")

splitters = []

for i, item in enumerate(lines[2:]):
    if i % 2 == 1: continue
    s = set()
    for index, c in enumerate(item):
        if c == "^":
            s.add(index)

    splitters.append(s)

beams = set([start])

ret = 0
for srow in splitters:
    nbeams = set()
    for b in beams:
        if b in srow:
            nbeams.add(b - 1)
            nbeams.add(b + 1)
            ret += 1
        else:
            nbeams.add(b)
    beams = nbeams

print(ret)