import aoc
contents = aoc.get_input(2025, 9).strip()
del aoc

# ---

points = list(map(tuple, (map(int, l.split(",")) for l in contents.split("\n")) ))

m = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x = abs(points[i][0] - points[j][0]) + 1
        y = abs(points[i][1] - points[j][1]) + 1

        m = max(x*y, m)

print(m)