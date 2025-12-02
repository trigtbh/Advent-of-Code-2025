import aoc
contents = aoc.get_input(2025, 2).strip()
del aoc

# ---
# part 1

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


print(f"Day 2 Part 1: {s}")
# ---
# part 2

s = 0

visited = set()

ranges = contents.split(",")
for r in ranges:
    lower, upper = map(int, r.split("-"))
    halfpoint = len(str(upper)) // 2
    bound = max(int(str(upper)[:halfpoint]), int(str(upper)[halfpoint:]))
    for i in range(1, bound+1):
        n = 2
        while True:
            # print(i, n)
            test = int(str(i)*n)
            # if lower <= test and test <= upper:
            if lower <= test <= upper and test not in visited:
                visited.add(test)
                # print(test)
                s += test
            n += 1
            if test > upper: break


print(f"Day 2 Part 2: {s}")