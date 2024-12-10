from collections import deque

with open ("input.txt", "r") as file:
    line = file.readline()

free_spaces = []  # num of spaces -> sorted array of start indices
max_space_string = 0
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

i = 0
while i < len(arr):
    if arr[i] == ".":
        start = i
        num = 0 
        while i < len(arr) and arr[i] == ".":
            num += 1
            i += 1
        free_spaces.append([num, start])
    else:
        i += 1
i = len(arr) - 1
while i >= 0:
    if arr[i] == ".":  # skip until the next char sequence
        i -= 1
        continue
    ch = arr[i]
    char_count = 0
    while arr[i] == ch:
        i -= 1
        char_count += 1
    index = -1
    spaces_used = -1
    space_index = -1
    for j in range(len(free_spaces)):
        spaces, idx = free_spaces[j]
        if idx < i and spaces >= char_count:
            index = idx
            spaces_used = spaces
            space_index = j
            break

    if index == -1:  # no spaces found
        continue

    for j in range(i + 1, i + 1 + char_count):
        arr[j] = "."
    for j in range(index, index + char_count):
        arr[j] = ch
    
    remaining_spaces = spaces_used - char_count
    if remaining_spaces > 0:
        free_spaces[space_index][0] = remaining_spaces
        free_spaces[space_index][1] = index + char_count
    else:
        free_spaces.pop(space_index)
res = 0
for i in range(len(arr)):
    if arr[i] != ".":
        res += arr[i] * i

print(res)