from pprint import pprint
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
    dx, dy = velocities[i]
    x += 100 * dx
    y += 100 * dy
    new_x = x % HEIGHT
    new_y = y % WIDTH
    grid[new_x][new_y] = grid[new_x][new_y] + 1 if grid[new_x][new_y] != "." else 1

    if new_x < HEIGHT // 2 and new_y < WIDTH // 2:
        q1 += 1
    elif new_x > HEIGHT // 2 and new_y < WIDTH // 2:
        q2 += 1
    elif new_x > HEIGHT // 2 and new_y > WIDTH // 2:
        q3 += 1
    elif new_x < HEIGHT // 2 and new_y > WIDTH // 2:
        q4 += 1
print(q1, q2, q3, q4)
res = q1 * q2 * q3 * q4
print(res)

