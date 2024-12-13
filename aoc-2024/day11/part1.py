

arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    arr = [int(i) for i in line.split(" ")]

for i in range(25):
    new_arr = []
    for num in arr:
        if num == 0:
            new_arr.append(1)
        elif len(str(num)) % 2 == 1:
            new_arr.append(num * 2024)
        else:
            num_str = str(num)
            new_arr.append(int(num_str[:len(num_str) // 2]))
            new_arr.append(int(num_str[len(num_str) // 2:]))
    arr = new_arr


print(len(arr))