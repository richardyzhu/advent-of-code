
with open ("input.txt", "r") as file:
    line = file.readline()

arr = []
add_space = False
counter = 0
for i in range(len(line)):
    num = int(line[i])
    for j in range(num):
        if add_space:
            arr.append(".")
        else:
            arr.append(counter)
    if add_space:
        add_space = False
    else:
        add_space = True
        counter += 1

l, r = 0, len(arr) - 1

while l < r:
    if arr[l] == ".":
        while r > l and arr[r] == ".":
            r -= 1
        if arr[r] == ".":
            break
        arr[l] = arr[r]
        arr[r] = "."
    l += 1

res = 0
for i in range(len(arr)):
    if arr[i] != ".":
        res += arr[i] * i

print(res)