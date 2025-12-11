import aoc
contents = aoc.get_input(2025, 11).strip()
del aoc

# ---

adj = {}

edges = []

nodes = set()

for line in contents.split("\n"):
    a, b = line.split(": ")
    # adj[a] = tuple(b.split(" "))
    for s in b.split(" "):
        edges.append((a, s))
        nodes |= set({a, s})

print(nodes)

def find(source, dest):
    n = len(edges)
    # graph = [[] for _ in range(n + 1)]
    # ind = {}

    graph = {n: [] for n in nodes}
    ind = {n: 0 for n in nodes}


    for u, v in edges:
        if u not in graph: graph[u] = []
        graph[u].append(v)
        if v not in ind: ind[v] = 0
        ind[v] += 1

    q = []
    for node in nodes:
        if ind[node] == 0:
            q.append(node)
    topo = []
    while q:
        n = q.pop(0)
        topo.append(n)
        for ne in graph[n]:
            ind[ne] -= 1
            if ind[ne] == 0:
                q.append(ne)
    
    ways = {n: 0 for n in nodes}
    ways[source] = 1

    for node in topo:
        for ne in graph[node]:
            if ne not in ways: ways[ne] = 0
            ways[ne] += ways[node]

    return ways[dest]

    
    
c = (find("svr", "fft") * find("fft", "dac") * find("dac", "out")) + (find("svr", "dac") * find("dac", "fft") * find("fft", "out")) 

print(c)