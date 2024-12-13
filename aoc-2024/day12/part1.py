
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
    perimeter = 0
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == ch:
            new_area, new_perimeter = traverse(nx, ny)
            area += new_area
            perimeter += new_perimeter
        else:
            perimeter += 1
    return area, perimeter

res = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (i, j) not in visited:
            area, perimeter = traverse(i, j)
            res += area * perimeter

print(res)