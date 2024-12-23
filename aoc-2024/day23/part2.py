from functools import cache
import sys

sys.setrecursionlimit(10000)

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

adj_idx = {}


for idx, i in enumerate(adj):
    adj_idx[idx] = i


cur_longest = []

@cache
def dfs(index, clique):
    if index >= 520:
        return
    s = adj_idx[index]
    for c in clique:
        if s not in adj[c]:
            dfs(index + 1, clique)
            return
    
    new_clique = list(clique)
    new_clique.append(s)
    new_clique.sort()

    if len(cur_longest) < len(new_clique):
        cur_longest = new_clique.copy()
    dfs(index + 1, tuple(new_clique))
    
    dfs(index + 1, clique)
    


for i in range(len(adj_idx)):
    for j in range(len(adj_idx)):
        # print(f"Processing {i} and {j}")
        dfs(j, (adj_idx[i],))


print(",".join(cur_longest))
