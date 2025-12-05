import aoc
contents = aoc.get_input(2025, 5).strip()
del aoc

# ---

ranges, vals = contents.split("\n\n")

r_full = []

for r in ranges.split("\n"):
    a, b = map(int, r.split("-"))
    r_full.append((a, b))

r_full = sorted(r_full)

r_complete = [r_full[0]]
for r in r_full[1:]:
    last = r_complete[-1]
    lasta, lastb = last

    newa, newb = r

    if lasta <= newa <= lastb:
        r_complete[-1] = (lasta, max(newb, lastb))
    else:
        r_complete.append(r)

s = 0
for r in r_complete:
    s += r[1] - r[0] + 1

print(s)