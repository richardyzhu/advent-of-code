
from collections import deque

grid = []
with open("input.txt", "r") as file:
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

res = 0
for start in starts:
    q = deque()
    q.append(start)
    cur_num = 0
    visited = set()
    visited.add(start)
    while q and cur_num < 9:
        cur_num += 1
        for i in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == cur_num and (new_x, new_y) not in visited:
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))
    res += len(q)

print(res)
