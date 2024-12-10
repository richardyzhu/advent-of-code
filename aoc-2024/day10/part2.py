
from collections import deque

grid = []
with open("test_input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        line_arr = [int(i) for i in list(line)]
        grid.append(line_arr)
        line = file.readline().replace("\n", "")

starts = []  # list of starting positions
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            starts.append((i, j))

res = [0]


def dfs(cur_num, x, y):
    if cur_num == 10:
        res[0] += 1
        return
    
    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        new_x, new_y = dx + x, dy + y
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == cur_num:
            dfs(cur_num + 1, new_x, new_y)

for x, y in starts:
    dfs(1, x, y)

print(res[0])
