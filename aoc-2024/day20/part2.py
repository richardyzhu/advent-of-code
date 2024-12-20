import heapq
from copy import deepcopy
grid = []

with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        grid.append(list(line))
        line = file.readline().replace("\n", "")

start = ()
end = ()
walls = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "E":
            end = (i, j)
        if grid[i][j] == "#":
            walls.append((i, j))


min_heap = [(0, end)]

dists_from_end = {end: 0}

while min_heap:
    dist, loc = heapq.heappop(min_heap)
    dists_from_end[loc] = dist
    x, y = loc
    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nx, ny = dx + x, dy + y
        if grid[nx][ny] == "#":
            continue
        new_dist = dist + 1
        if (nx, ny) not in dists_from_end or dists_from_end[(nx, ny)] > new_dist:
            heapq.heappush(min_heap, (dist + 1, (nx, ny)))

count = 0

def get_all_available_cheats(start_index, num_moves, cheats):
    if num_moves == 21:
        return
    if start_index in cheats and num_moves >= cheats[start_index]:
        return

    cheats[start_index] = num_moves
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        new_index = (start_index[0] + dx, start_index[1] + dy)
        get_all_available_cheats(new_index, num_moves + 1, cheats)
    return cheats

for loc in dists_from_end:
    x, y = loc
    cheats = {}
    get_all_available_cheats(loc, 0, cheats)   
    for cheat in cheats:
        dist = cheats[cheat]
        nx, ny = cheat
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) in dists_from_end:
            if dists_from_end[(nx, ny)] - dists_from_end[loc] >= 100 + dist:
                count += 1

print(count)
    