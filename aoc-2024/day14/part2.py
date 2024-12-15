from pprint import pprint
from copy import deepcopy
positions = []
velocities = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        left, right = line.split(" ")
        nums = left.split("=")[1]
        x, y = int(nums.split(",")[1]), int(nums.split(",")[0])
        positions.append([x, y])
        nums = right.split("=")[1]
        x, y = int(nums.split(",")[1]), int(nums.split(",")[0])
        velocities.append([x, y])
        line = file.readline()


q1 = q2 = q3 = q4 = 0

WIDTH = 101  # 101
HEIGHT = 103  # 103

grid = [["."] * WIDTH for i in range(HEIGHT)]
for i in range(len(positions)):
    x, y = positions[i]
    grid[x][y] = str(int(grid[x][y]) + 1) if grid[x][y] != "." else "1"


possible_grids = []

def count_area(x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == ".":
        return 0
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    
    return 1 + count_area(x + 1, y, visited) + count_area(x, y + 1, visited) + count_area(x - 1, y, visited) + count_area(x, y - 1, visited)

for j in range(10403):
    max_area = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "." and (r, c) not in visited:
                max_area = max(max_area, count_area(r, c, visited))

    if max_area > 25:
        new_grid = deepcopy(grid)
        possible_grids.append((j, new_grid))
    
    for i in range(len(positions)):
        x, y = positions[i]
        orig_x, orig_y = x, y
        dx, dy = velocities[i]
        x += dx
        y += dy
        new_x = x % HEIGHT
        new_y = y % WIDTH
        grid[orig_x][orig_y] = str(int(grid[orig_x][orig_y]) - 1) if grid[orig_x][orig_y] != "1" else "."
        grid[new_x][new_y] = str(int(grid[new_x][new_y]) + 1) if grid[new_x][new_y] != "." else "1"
        
        positions[i] = [new_x, new_y]
    
for grids in possible_grids:
    possible_grid = grids[1]
    print(f"Iteration {grids[0]}:")
    for row in possible_grid:
        for ch in row:
            if ch != ".":
                print("#", end="")
            else:
                print(".", end="")
        print("\n", end="")

