
connections = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        connections.append(tuple(line.split("-")))
        line = file.readline().replace("\n", "")


adj = {}

for a, b in connections:
    adj[a] = adj.get(a, []) + [b]
    adj[b] = adj.get(b, []) + [a]
sets = set()

for a in adj:
    for b in adj[a]:
        for c in adj[b]:
            for d in adj[c]:
                if d == a:
                    arr = [a, b, c]
                    if a[0] == 't' or b[0] == 't' or c[0] == 't':
                        arr.sort()
                        trio_str = ",".join(arr)
                        sets.add(trio_str)
print(len(sets))