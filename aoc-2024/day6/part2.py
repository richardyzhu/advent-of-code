from copy import deepcopy
grid = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        grid.append(list(line))
        line = file.readline().replace("\n", "")

pos = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            pos = [i, j]
            break
start = pos.copy()
visited = set()
dir = [-1, 0]
while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid):
    if grid[pos[0]][pos[1]] == '#':
        pos[0] -= dir[0]
        pos[1] -= dir[1]
        if dir[0] == -1 and dir[1] == 0:
            dir[0] = 0
            dir[1] = 1
        elif dir[0] == 0 and dir[1] == 1:
            dir[0] = 1
            dir[1] = 0
        elif dir[0] == 1 and dir[1] == 0:
            dir[0] = 0
            dir[1] = -1
        else:
            dir[0] = -1
            dir[1] = 0
    visited.add(tuple(pos))
    pos[0] += dir[0]
    pos[1] += dir[1]

visited.remove(tuple(start))
counter = 0
for new_pos in visited:
    new_pos = list(new_pos)
    new_grid = deepcopy(grid)
    new_grid[new_pos[0]][new_pos[1]] = '#'
    new_visited = set()
    total_visited = 0
    dir = [-1, 0]
    pos = start.copy()
    while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid) and total_visited < 2 * len(grid) * len(grid[0]):
        if new_grid[pos[0]][pos[1]] == '#':
            pos[0] -= dir[0]
            pos[1] -= dir[1]
            if dir[0] == -1 and dir[1] == 0:
                dir[0] = 0
                dir[1] = 1
            elif dir[0] == 0 and dir[1] == 1:
                dir[0] = 1
                dir[1] = 0
            elif dir[0] == 1 and dir[1] == 0:
                dir[0] = 0
                dir[1] = -1
            else:
                dir[0] = -1
                dir[1] = 0
        total_visited += 1
        pos[0] += dir[0]
        pos[1] += dir[1]
    if total_visited == 5 * len(grid) * len(grid[0]):
        counter += 1

print(counter)