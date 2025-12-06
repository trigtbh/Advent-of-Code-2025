import aoc
contents = aoc.get_input(2025, 6)
del aoc

# ---


lines = contents.split("\n")
# grid = [[x for x in l.split(" ") if x] for l in lines]

ml = max(len(l) for l in lines)
lines = [
    l + " " * (ml - len(l)+1)
    for l in lines
]

ret = 0
cpointer = 0
while cpointer < len((lines[-1])):
    i = cpointer+1 
    while i < len(lines[-1]) and lines[-1][i] == " ":
        i += 1

    op = lines[-1][cpointer]

    ns = []
    for x in range(cpointer, i-1):
        s = ""
        for ri in range(len(lines) - 2, -1, -1):
            s = lines[ri][x] + s
        ns.append(int(s.strip()))

    s = 0
    if op == "+":
        for n in ns:
            s += n
    else:
        s = 1
        for n in ns:
            s *= n
    ret += s


    cpointer = i

print(ret)