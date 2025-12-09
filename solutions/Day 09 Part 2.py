import aoc
contents = aoc.get_input(2025, 9).strip()
del aoc

# ---
points = list(map(tuple, (map(int, l.split(",")) for l in contents.split("\n")) ))

walls = []

for i in range(len(points)):
    walls.append(
        (points[i], points[(i+1)%len(points)])
    )


def intersect(p1, p2, w1, w2):
    if p1[0] == p2[0]: # vertical line
        if w1[0] == w2[0]: 
            return False
        return ((p1[1] <= w1[1] <= p2[1]) or (p2[1] <= w1[1] <= p1[1])) and ((w1[0] <= p1[0] <= w2[0]) or (w2[0] <= p1[0] <= w1[0]) )

    else:
        if w1[1] == w2[1]: 
            return False
        return ((p1[0] <= w1[0] <= p2[0]) or (p2[0] <= w1[0] <= p1[0])) and ((w1[1] <= p1[1] <= w2[1]) or (w2[1] <= p1[1] <= w1[1])) 


m = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        if p1[0] == p2[0] or p1[1] == p2[1]: continue

        good = True

        side1 = (p1, (p1[0], p2[1]))
        side2 = ((p1[0], p2[1]), p2)
        side3 = (p2, (p2[0], p1[1]))
        side4 = ((p2[0], p1[1]), p1)

        flag = (p1 in {(9,5),(2,3)} and p2 in {(9,5),(2,3)} )

        for (w1, w2) in walls:
            if {p1, p2} & {w1, w2}:
                continue
            if intersect(*side1, w1, w2):
                good = False
                if flag: print(side1, (w1, w2))
                break
            if intersect(*side2, w1, w2):
                good = False
                if flag: print(side2, (w1, w2))
                break
            if intersect(*side3, w1, w2):
                good = False
                if flag: print(side3, (w1, w2))
                break
            if intersect(*side4, w1, w2):
                good = False
                if flag: print(side4, (w1, w2))
                break
            


        if good:
            x = abs(p1[0] - p2[0]) + 1
            y = abs(p1[1] - p2[1]) + 1

            a = x*y
            if a > m:
                m = a
        
print(m)