import heapq

grid = [["."] * 71 for i in range(71)]
bytes = []
with open("input.txt", "r") as file:
    temp = 0
    line = file.readline()
    while line:
        arr = line.split(",")
        y = int(arr[0])
        x = int(arr[1])
        bytes.append((x, y))
        if temp < 1024:
            grid[x][y] = "#"
        temp += 1
        line = file.readline()

counter = 1024
while True:
    new_wall = bytes[counter]
    grid[new_wall[0]][new_wall[1]] = "#"
    counter += 1
    min_heap = [(0, (0, 0))]
    dists = {}
    while min_heap:
        dist, coord = heapq.heappop(min_heap)
        x, y = coord
        if coord in dists and dists[coord] >= dist:
            continue
        dists[coord] = dist
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and grid[nx][ny] != "#":
                if (nx, ny) in dists and dists[(nx, ny)] <= dist + 1:
                    continue
                heapq.heappush(min_heap, (dist + 1, (nx, ny)))
    if (70, 70) not in dists:
        break

print(bytes[counter - 1])