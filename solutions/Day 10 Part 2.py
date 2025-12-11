import aoc
contents = aoc.get_input(2025, 10).strip()
del aoc

# ---

def find_pivot(row):
    for c in range(len(row)):
        if not basically_zero(row[c]):
            return c
    return len(row)

def count_pivot(row):
    c = 0
    for item in row:
        if item != 0:
            c += 1
    return c

print_consolidate_errors = False

def consolidate(A):
    coeffs = {}
    for i, r in enumerate(A):
        c = r[:-1]
        v = r[-1]
        c = tuple(c)

        if not any(c) and not basically_zero(v):
            if print_consolidate_errors: print(f"1 c in row {i+1}")
            return None

        if c not in coeffs:
            if basically_zero(v):
                coeffs[c] = 0
            else:
                coeffs[c] = v
        else:
            if basically_zero(v) and basically_zero(coeffs[c]):
                continue


            if abs(coeffs[c] - v) > 1e-4:
                if print_consolidate_errors: print(f"2 c in row {i+1}")
                return None
            else:
                del r
    try:
        A = sorted(A, key=lambda r: (-find_pivot(r), count_pivot(r)), reverse=True)
    except:
        A = sorted(A, key=lambda r: find_pivot(r))
    return A


def basically_zero(x):
    return abs(x) < 1e-5

def print_matrix(A):
    for r in A:
        print(" ".join(map(str, r)))


def solve_system(eqs, b):
    A = []

    for i in range(len(b)):
        r = []
        needed = False
        for eq in eqs:
            if i in eq:
                needed = True
                r.append(1)
            else:
                r.append(0)
        if not needed and not basically_zero(b[i]): 
            return None
        r.append(b[i])
        A.append(r)

    ncols = len(A[0]) - 1
    nrows = len(A)

    pivot = 0

    for col in range(ncols):
        if pivot >= len(A): break

        cand = -1

        for r in range(pivot, len(A)):
            if not basically_zero(A[r][col]):
                cand = r
                break
        if cand == -1: continue
        A[cand], A[pivot] = A[pivot], A[cand]
        scalar = A[pivot][col]
        for c in range(len(A[0])):
            A[pivot][c] /= scalar

        for r in range(nrows):
            if r == pivot: continue

            f = A[r][col]
            if not basically_zero(f):
                for c in range(col, len(A[0])):
                    A[r][c] -= f * A[pivot][c]

        pivot += 1

    
    for r in range(len(A)):
        for c in range(len(A[0])):
            if basically_zero(A[r][c]):
                A[r][c] = 0


    mapped = {}

    for r in A:
        allzeros = all(basically_zero(v) for v in r[:-1])
        if allzeros and not basically_zero(r[-1]):
            return None


        mapped[tuple(r[:-1])] = r[-1]




    for r in A:
        row = r[:-1]
        v = r[-1]
        nonzero = len(row) - row.count(0)

    rank = sum(1 for r in A if not all(basically_zero(v) for v in r[:-1]))
    free_vars = len(eqs) - rank
    if free_vars > 0:

        m = float("inf")

        coef_temp = [0] * free_vars
        thresh = max(b)
        pivot_cols = set()
        for row_idx in range(len(A)):
            for col_idx in range(len(eqs)):
                if abs(A[row_idx][col_idx] - 1.0) < 1e-6:
                    if all(basically_zero(A[row_idx][c]) for c in range(col_idx)):
                        pivot_cols.add(col_idx)
                        break

        free_var_indices = [i for i in range(len(eqs)) if i not in pivot_cols]

        while coef_temp != [thresh] * free_vars:
            check = []
            for ri in range(len(A)):
                someval = A[ri][-1]
                for fi in range(free_vars):
                    someval -= A[ri][ free_var_indices[fi] ] * coef_temp[fi]
                check.append(someval)
            g = True
            for v in check:
                if not basically_zero(abs(v - round(v))):
                    g = False
                    break
                if v < 0: 
                    g = False
                    break
            if g:
                button_presses = [0] * len(eqs)
                
                for row_idx in range(len(A)):
                    for col_idx in range(len(eqs)):
                        if abs(A[row_idx][col_idx] - 1.0) < 1e-6:
                            if all(basically_zero(A[row_idx][c]) for c in range(col_idx)):
                                button_presses[col_idx] = check[row_idx]
                                break
                for fi in range(free_vars):
                    button_presses[free_var_indices[fi]] = coef_temp[fi]    

                pairs = {}
                for idx, button_tuple in enumerate(eqs):
                    pairs[button_tuple] = button_presses[idx]

                final_check = [0] * len(b)
                for k, v in pairs.items():
                    if not basically_zero(v) and v < 0:
                        return None
                    for index in k:
                        final_check[index] += v
                
                if not all(basically_zero(final_check[i] - b[i]) for i in range(len(b))):
                    g = False

                if g:
                    m = min(m, sum(button_presses))

            for i in range(len(coef_temp) - 1, -1, -1):
                coef_temp[i] += 1
                if coef_temp[i] <= thresh:
                    break
                coef_temp[i] = 0


        if m != float("inf"):
            if not basically_zero(abs(m - round(m))): return None
            return m
        else:
            return None
        
    else:
        s = 0
        for r in A:
            if not basically_zero(abs(r[-1] - round(r[-1]))): return None
            if r[-1] < 0: return None
            s += r[-1]
        return round(s)





ret = 0

i = 0
for line in contents.split("\n"):
    i += 1
    tokens = line.split(" ")
    p = tokens[-1][1:-1]
    
    p = p.split(",")
    p = tuple(map(int, p))
    
    buttons = tokens[1:-1]
    buttons = [t[1:-1].split(",") for t in buttons]
    buttons = [tuple(map(int, t)) for t in buttons]
    
    minima = float("inf")
    for n in range(0, 2 ** (len(buttons))):
        b = bin(n)[2:]
        b = "0" * (len(buttons) - len(b)) + b
        used = []

        for cindex, c in enumerate(b):
            if c == "1":
                used.append(buttons[cindex])

        attempt = solve_system(used, p)
        if attempt:
            minima = min(minima, attempt)

    if minima == float("inf"):
        print(i)
        raise ValueError
    ret += minima
            


print(round(ret))