import aoc
contents = aoc.get_input(2025, 11).strip()
del aoc

# ---

adj = {}

for line in contents.split("\n"):
    a, b = line.split(": ")
    adj[a] = tuple(b.split(" "))

visited = set()

queue = ["you"]

c = 0
while len(queue) > 0:
    curr = queue.pop(0)
    if curr == "out": 
        c += 1
        continue
    for n in adj[curr]:
        if n not in visited:
            queue.append(n)

    visited.add(curr)

print(c)