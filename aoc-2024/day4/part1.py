

input_arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        input_arr.append(list(line))
        line = file.readline()

res = 0

for i in range(len(input_arr)):
    for j in range(len(input_arr[i])):
        if input_arr[i][j] == 'X':
            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
            for dx, dy in dirs:
                for k in range(1, 4):
                    new_x = dx * k + i
                    new_y = dy * k + j
                    if 0 <= new_x < len(input_arr) and 0 <= new_y < len(input_arr[0]):
                        if k == 1 and input_arr[new_x][new_y] == 'M':
                            continue
                        if k == 2 and input_arr[new_x][new_y] == 'A':
                            continue
                        if k == 3 and input_arr[new_x][new_y] == 'S':
                            res += 1
                            continue
                        break

print(res)


