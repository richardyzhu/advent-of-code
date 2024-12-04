input_arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        input_arr.append(list(line))
        line = file.readline()

res = 0
for i in range(1, len(input_arr) - 1):
    for j in range(1, len(input_arr[0]) - 1):
        if input_arr[i][j] == 'A':
            if input_arr[i-1][j-1] == 'M' and input_arr[i+1][j+1] == 'S' and input_arr[i+1][j-1] == 'M' and input_arr[i-1][j+1] == 'S':
                res += 1
            if input_arr[i-1][j-1] == 'S' and input_arr[i+1][j+1] == 'M' and input_arr[i+1][j-1] == 'M' and input_arr[i-1][j+1] == 'S':
                res += 1
            if input_arr[i-1][j-1] == 'M' and input_arr[i+1][j+1] == 'S' and input_arr[i+1][j-1] == 'S' and input_arr[i-1][j+1] == 'M':
                res += 1
            if input_arr[i-1][j-1] == 'S' and input_arr[i+1][j+1] == 'M' and input_arr[i+1][j-1] == 'S' and input_arr[i-1][j+1] == 'M':
                res += 1

print(res)