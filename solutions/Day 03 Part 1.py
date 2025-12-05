import aoc
contents = aoc.get_input(2025, 3).strip()
del aoc

# ---

s = 0
for line in contents.split("\n"):
    m = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            m = max(m, int(line[i] + line[j]))

    s += m

print(s)