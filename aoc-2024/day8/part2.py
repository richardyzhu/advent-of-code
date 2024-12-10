input_arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        input_arr.append(list(line))
        line = file.readline().replace("\n", "")

antennas = {}  # char -> positions
for i in range(len(input_arr)):
    for j in range(len(input_arr[0])):
        if input_arr[i][j] != ".":
            antennas[input_arr[i][j]] = antennas.get(input_arr[i][j], []) + [[i, j]]

antinodes = set()  # positions
for antenna in antennas:
    positions = antennas[antenna]
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x_diff = positions[i][0] - positions[j][0]
            y_diff = positions[i][1] - positions[j][1]
            new_x1 = positions[i][0]
            new_y1 = positions[i][1]
            new_x2 = positions[j][0]
            new_y2 = positions[j][1]
            while 0 <= new_x1 < len(input_arr) and 0 <= new_y1 < len(input_arr[0]):
                antinodes.add((new_x1, new_y1))
                new_x1 += x_diff
                new_y1 += y_diff
            while 0 <= new_x2 < len(input_arr) and 0 <= new_y2 < len(input_arr[0]):
                antinodes.add((new_x2, new_y2))
                new_x2 -= x_diff
                new_y2 -= y_diff

print(antinodes)
print(len(antinodes))
