import aoc
contents = aoc.get_input(2025, 1).strip()
del aoc

# ---
# part 1

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


# part 2
s = 0

n = 50
lines = contents.split("\n")
for l in lines:
    c = l[0]
    change = int(l[1:])
    ccp = change
    s += (change // 100)
    change %= 100
    if change > 0:
        if c == "L":
            n += change
            if n >= 100: 
                s += 1
        else:
            gt = (n > 0)
            n -= change
            if n <= 0 and gt:
                s += 1
    n %= 100


print(s)
    