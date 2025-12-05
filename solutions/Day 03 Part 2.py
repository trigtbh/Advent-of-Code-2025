import aoc
contents = aoc.get_input(2025, 3).strip()
del aoc

# ---

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

print(s)