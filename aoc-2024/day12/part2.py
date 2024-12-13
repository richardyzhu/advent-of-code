
arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        arr.append(list(line))
        line = file.readline().replace("\n", "")

prices = {}
visited = set()

def traverse(x, y):
    if (x, y) in visited:
        return 0, 0
    visited.add((x, y))
    ch = arr[x][y]
    area = 1
    all_sides = set()
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == ch:
            new_area, new_sides = traverse(nx, ny)
            area += new_area
            if new_sides:
                all_sides = all_sides.union(new_sides)
        else:
            all_sides.add((dx, dy, nx, ny))
    return area, all_sides

def traverse_sides(old_x, old_y, x, y, visited_sides):
    if (old_x, old_y, x, y) in visited_sides:
        return

    visited_sides.add((old_x, old_y, x, y))
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy
        if (old_x, old_y, nx, ny) in all_sides:
            traverse_sides(old_x, old_y, nx, ny, visited_sides)

res = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (i, j) not in visited:
            area, all_sides = traverse(i, j)
            num_sides = 0
            visited_sides = set()
            for old_x, old_y, x, y in all_sides:
                if (old_x, old_y, x, y) not in visited_sides:
                    traverse_sides(old_x, old_y, x, y, visited_sides)
                    num_sides += 1
            res += area * num_sides

print(res)