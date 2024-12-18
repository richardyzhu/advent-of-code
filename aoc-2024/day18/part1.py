import heapq

grid = [["."] * 71 for i in range(71)]
with open("input.txt", "r") as file:
    for i in range(1024):
        line = file.readline()
        arr = line.split(",")
        y = int(arr[0])
        x = int(arr[1])
        grid[x][y] = "#"
        print(y, x)


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

print(dists[(70, 70)])
