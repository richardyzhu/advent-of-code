
grid = []
moves = ""
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line and len(line) > 1:
        grid.append(list(line))
        line = file.readline().replace("\n", "")
    line = file.readline()
    while line:
        moves += (line.replace("\n", ""))
        line = file.readline()

pos = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            pos = [i, j]

for i in range(len(moves)):
    move = moves[i]
    dir = [0, 0]
    if move == ">":
        dir = [0, 1]
    elif move == "<":
        dir = [0, -1]
    elif move == "^":
        dir = [-1, 0]
    else:
        dir = [1, 0]
    
    box_len = 0
    cur_loc = [pos[0], pos[1]]
    while grid[cur_loc[0] + dir[0]][cur_loc[1] + dir[1]] == "O":
        box_len += 1
        cur_loc[0] += dir[0]
        cur_loc[1] += dir[1]
    
    if grid[cur_loc[0] + dir[0]][cur_loc[1] + dir[1]] == "#":
        continue
    
    if box_len > 0:
        grid[cur_loc[0] + dir[0]][cur_loc[1] + dir[1]] = "O"
    pos[0] += dir[0]
    pos[1] += dir[1]
    grid[pos[0]][pos[1]] = "@"

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            res += 100 * i + j

print(res)
