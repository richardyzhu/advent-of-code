from functools import cache
arr = []
inputs = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    arr = line.split(", ")
    line = file.readline()
    line = file.readline().replace("\n", "")
    while line:
        inputs.append(line)
        line = file.readline().replace("\n", "")

patterns = set(arr)

@cache
def recurse(design, cur_index, cur_str):
    if cur_index == len(design) and not cur_str:
        return True
    elif cur_index == len(design) and cur_str:
        return False
    
    cur_str += design[cur_index]
    if cur_str in patterns:
        return recurse(design, cur_index + 1, "") or recurse(design, cur_index + 1, cur_str)
    else:
        return recurse(design, cur_index + 1, cur_str)

counter = 0
for i in inputs:
    if recurse(i, 0, ""):
        counter += 1

print(counter)
