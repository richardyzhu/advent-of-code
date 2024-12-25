
inputs = []

with open("input.txt", "r") as file:
    line = "temp"
    while line:
        inputs.append([])
        for i in range(7):
            line = file.readline().replace("\n", "")
            inputs[-1].append(list(line))
        line = file.readline()

res = 0
for i in range(len(inputs) - 1):
    for j in range(i + 1, len(inputs)):
        grid1 = inputs[i]
        grid2 = inputs[j]
        used = set()
        overlap = False
        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                if grid1[r][c] == "#":
                    used.add((r, c))
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == "#":
                    if (r, c) in used:
                        overlap = True
                        break
                    used.add((r, c))
        if overlap:
            continue
        res += 1

print(res)