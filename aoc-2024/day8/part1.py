
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
            x_diff = abs(positions[i][0] - positions[j][0])
            y_diff = abs(positions[i][1] - positions[j][1])
            used = set()
            used.add((positions[i][0], positions[i][1]))
            used.add((positions[j][0], positions[j][1]))
            anti1 = (positions[i][0] - x_diff, positions[i][1] - y_diff)
            anti2 = (positions[i][0] + x_diff, positions[i][1] + y_diff)
            anti3 = (positions[j][0] - x_diff, positions[j][1] - y_diff)
            anti4 = (positions[j][0] + x_diff, positions[j][1] + y_diff)
            count = 0
            if anti1 not in used and 0 <= anti1[0] < len(input_arr) and 0 <= anti1[1] < len(input_arr[0]):
                antinodes.add(anti1)
                count += 1
            if anti2 not in used and 0 <= anti2[0] < len(input_arr) and 0 <= anti2[1] < len(input_arr[0]):
                antinodes.add(anti2)
                count += 1
            if anti3 not in used and 0 <= anti3[0] < len(input_arr) and 0 <= anti3[1] < len(input_arr[0]):
                antinodes.add(anti3)
                count += 1
            if anti4 not in used and 0 <= anti4[0] < len(input_arr) and 0 <= anti4[1] < len(input_arr[0]):
                antinodes.add(anti4)
                count += 1
            if count == 4:
                print(used)
                print(anti1)
                print(anti2)
                print(anti3)
                print(anti4)
print(antinodes)
print(len(antinodes))
