
temp_grid = []
moves = ""
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line and len(line) > 1:
        temp_grid.append(list(line))
        line = file.readline().replace("\n", "")
    line = file.readline()
    while line:
        moves += (line.replace("\n", ""))
        line = file.readline()

grid = []

for i in range(len(temp_grid)):
    grid.append([])
    for j in range(len(temp_grid[0])):
        if temp_grid[i][j] == "#":
            grid[i].append("#")
            grid[i].append("#")
        elif temp_grid[i][j] == "@":
            grid[i].append("@")
            grid[i].append(".")
        elif temp_grid[i][j] == ".":
            grid[i].append(".")
            grid[i].append(".")
        else:
            grid[i].append("[")
            grid[i].append("]")


pos = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            pos = [i, j]



def can_move(dir, cur_loc, symbol_dict):
    if grid[cur_loc[0]][cur_loc[1]] == "#":
        return False

    if grid[cur_loc[0]][cur_loc[1]] == ".":
        symbol_dict[(cur_loc[0], cur_loc[1])] = "."
        return True

    if grid[cur_loc[0]][cur_loc[1]] == "[":
        symbol_dict[(cur_loc[0], cur_loc[1])] = "["
        symbol_dict[(cur_loc[0], cur_loc[1] + 1)] = "]"
        return can_move(dir, [cur_loc[0] + dir[0], cur_loc[1] + dir[1]], symbol_dict) and can_move(dir, [cur_loc[0] + dir[0], cur_loc[1] + dir[1] + 1], symbol_dict)
    elif grid[cur_loc[0]][cur_loc[1]] == "]":
        symbol_dict[(cur_loc[0], cur_loc[1])] = "]"
        symbol_dict[(cur_loc[0], cur_loc[1] - 1)] = "["
        return can_move(dir, [cur_loc[0] + dir[0], cur_loc[1] + dir[1]], symbol_dict) and can_move(dir, [cur_loc[0] + dir[0], cur_loc[1] + dir[1] - 1], symbol_dict)
    else:
        symbol_dict[(cur_loc[0], cur_loc[1])] = "@"
        return can_move(dir, [cur_loc[0] + dir[0], cur_loc[1] + dir[1]], symbol_dict)
    

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
    box_width = 1
    box_left = [pos[0], pos[1]]
    cur_loc = [pos[0], pos[1]]
    if dir == [0, -1] or dir == [0, 1]:
        while grid[cur_loc[0] + dir[0]][cur_loc[1] + dir[1]] == "]" or grid[cur_loc[0] + dir[0]][cur_loc[1] + dir[1]] == "[":
            box_len += 1
            cur_loc[0] += dir[0]
            cur_loc[1] += dir[1]
        if grid[cur_loc[0] + dir[0]][cur_loc[1] + dir[1]] == "#":
            continue
        cur_loc[0] += dir[0]
        cur_loc[1] += dir[1]
        for y in range(box_len + 1):
            grid[cur_loc[0]][cur_loc[1]] = grid[cur_loc[0]][cur_loc[1] - dir[1]]
            cur_loc[0] -= dir[0]
            cur_loc[1] -= dir[1]
        grid[cur_loc[0]][cur_loc[1]] = "."
    else:
        symbol_dict = {}
        valid = can_move(dir, cur_loc, symbol_dict)
        if not valid:
            continue
        for loc in symbol_dict:
            old_loc = (loc[0] - dir[0], loc[1] - dir[1])
            if old_loc in symbol_dict:
                grid[loc[0]][loc[1]] = symbol_dict[old_loc]
            else:
                grid[loc[0]][loc[1]] = "."

    pos[0] += dir[0]
    pos[1] += dir[1]


res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            res += 100 * i + j

print(res)
