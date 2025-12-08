import aoc
contents = aoc.get_input(2025, 8).strip()
del aoc

# ---

points = list(map(tuple, (map(int, x.split(",")) for x in contents.split("\n"))))

groups = {}

def distance(d1, d2):
    return (
        (d1[0]-d2[0])**2 +
        (d1[1]-d2[1])**2 +
        (d1[2]-d2[2])**2 
    ) ** 0.5


s = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        s.append((i, j))


s = sorted(s, key=lambda t: distance(points[t[0]], points[t[1]]))

visited = set()

for i in range(len(points)):
    groups[i] = set({i})

for pair in s[:1000]:
    a, b = pair
    # if a in visited: 
        # continue
    # print(pair)
    if a not in groups and b not in groups:
        nset = set()
        nset.add(a)
        nset.add(b)
        groups[a] = nset
        groups[b] = nset

    elif a not in groups:
        groups[a] = groups[b]
        groups[a].add(a)

    elif b not in groups:
        groups[b] = groups[a]
        groups[b].add(b)

    else:
        joined = groups[b] | groups[a]
        joined.add(b)
        joined.add(a)

        for connected in groups[a]:
            groups[connected] = joined
        for connected in groups[b]:
            groups[connected] = joined

    visited.add(a)

final = set()
for group in groups.values():
    final.add(frozenset(group))



final = sorted(final, key=lambda x: len(x), reverse=True)


final = [len(s) for s in final]
# print(final)

print(final[0] * final[1] * final[2])