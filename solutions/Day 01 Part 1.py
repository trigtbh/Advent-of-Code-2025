import aoc
contents = aoc.get_input(2025, 1).strip()
del aoc

# ---

s = 0

n = 50
lines = contents.split("\n")
for l in lines:
    c = l[0]
    change = int(l[1:])
    if c == "L":
        n += change
    else:
        n -= change
    n %= 100
    if n == 0: 
        s += 1

print(s)