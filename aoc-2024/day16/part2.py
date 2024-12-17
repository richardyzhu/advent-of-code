import heapq
import sys

sys.setrecursionlimit(10000)

grid = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        grid.append(list(line))
        line = file.readline().replace("\n", "")

min_points = [float("inf")]

start_pos = [0, 0]
end_pos = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start_pos[0] = i
            start_pos[1] = j
        if grid[i][j] == 'E':
            end_pos[0] = i
            end_pos[1] = j


min_heap = [(0, tuple(start_pos), (0, 1), (tuple(start_pos), (0, 1)))]  # dist, position, direction
min_dists = {}

while min_heap:
    dist, pos, direction, prev = heapq.heappop(min_heap)
    pos_dir = (pos, direction)
    if pos_dir not in min_dists:
        min_dists[pos_dir] = (dist, [prev])
    else:
        if dist > min_dists[pos_dir][0]:
            continue
        if min_dists[pos_dir][0] > dist:
            min_dists[pos_dir] = (dist, [prev])
        else:
            min_dists[pos_dir][1].append(prev)

    x, y = pos
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if dx == direction[0] * -1 and dy == direction[1] * -1:
            continue

        if dx == direction[0] and dy == direction[1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                heapq.heappush(min_heap, (dist + 1, (nx, ny), (dx, dy), ((x, y), (direction[0], direction[1]))))
        else:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                heapq.heappush(min_heap, (dist + 1001, (nx, ny), (dx, dy), ((x, y), (direction[0], direction[1]))))

end_pos = tuple(end_pos)
min_dist = float("inf")
end_pos_dir = ()
for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if min_dist > min_dists.get((end_pos, direction), (float("inf"), ()))[0]:
        min_dist = min_dists.get((end_pos, direction), (float("inf"), ()))[0]
        end_pos_dir = (end_pos, direction)
on_shortest_path = set()
on_shortest_path_direction = set()

def dfs(cur_pos, cur_dir):
    if (cur_pos, cur_dir) in on_shortest_path_direction:
        return
    on_shortest_path.add(cur_pos)
    on_shortest_path_direction.add((cur_pos, cur_dir))
    if cur_pos == start_pos:
        return
    prev_pos = min_dists[(cur_pos, cur_dir)][1]
    for prev in prev_pos:
        dfs(prev[0], prev[1])
dfs(end_pos_dir[0], end_pos_dir[1])
print(len(on_shortest_path))