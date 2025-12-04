import aoc
day = 3
contents = aoc.get_input(2025, day).strip()
del aoc

# ---
# part 1

s = 0
for line in contents.split("\n"):
    m = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            m = max(m, int(line[i] + line[j]))

    s += m




print(f"Day {day} Part 1: {s}")


# ---
# part 2

counted = 12

s = 0
for line in contents.split("\n"):
    m = 0
    last = -1
    for pointer in range(counted):

        mval = 0
        mindex = -1

        for p in range(len(line) - counted + pointer, last, -1):
            if int(line[p]) >= mval:
                mval = int(line[p])
                mindex = p
        last = mindex
        m = m * 10 + mval
    s += m


print(f"Day {day} Part 2: {s}")