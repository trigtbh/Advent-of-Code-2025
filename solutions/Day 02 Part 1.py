import aoc
contents = aoc.get_input(2025, 2).strip()
del aoc

# ---

s = 0

ranges = contents.split(",")
for r in ranges:
    lower, upper = map(int, r.split("-"))
    halfpoint = len(str(upper)) // 2
    bound = max(int(str(upper)[:halfpoint]), int(str(upper)[halfpoint:]))
    for i in range(bound+1):
        test = int(str(i) + str(i))
        # if lower <= test and test <= upper:
        if lower <= test <= upper:
            s += test

print(s)