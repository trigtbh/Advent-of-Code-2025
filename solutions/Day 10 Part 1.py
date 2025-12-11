import aoc
contents = aoc.get_input(2025, 10).strip()
del aoc

# ---
ret = 0

ind = 0
for line in contents.split("\n"):
    ind += 1
    tokens = line.split(" ")
    p = tokens[0][1:-1]
    buttons = tokens[1:-1]
    buttons = [t[1:-1].split(",") for t in buttons]
    buttons = [tuple(map(int, t)) for t in buttons]

    b_final = []
    for button in buttons:
        s = ""
        for i in range(len(p)):
            if i in button:
                s += "1"
            else:
                s += "0"
        b_final.append(int(s, 2))

    buttons = b_final

    target = ""
    for i in range(len(p)):
        if p[i] == "#":
            target += "1"
        else:
            target += "0"
    target = int(target, 2)

    mincheck = float("inf")

    for n in range(2 ** len(buttons)):
        b = bin(n)[2:]
        b = "0" * (len(buttons) - len(b)) + b
        check = 0
        temp = 0
        used = []
        for cindex, character in enumerate(b):
            if character == "1":
                temp += 1
                used.append(cindex)
                check ^= buttons[cindex]
        if check == target:
            mincheck = min(temp, mincheck)

    ret += mincheck

print(ret)