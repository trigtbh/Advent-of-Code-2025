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

beams = {start: 1}

ret = 0
for srow in splitters:
    nbeams = {}
    for b in beams:
        if b in srow:
            # nbeams.append(b - 1)
            if (b - 1) not in nbeams:
                nbeams[b-1] = 0
            nbeams[b-1] += beams[b]
            # nbeams.append(b + 1)
            if (b + 1) not in nbeams:
                nbeams[b+1] = 0
            nbeams[b+1] += beams[b]
        else:
            # nbeams.append(b)

            if b not in nbeams:
                nbeams[b] = 0

            nbeams[b] += beams[b]
    beams = nbeams
    ret += 1

print(sum(beams.values()))