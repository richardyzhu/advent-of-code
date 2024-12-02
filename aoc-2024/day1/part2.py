
ids_left = []
ids_right = []

with open('input.txt', 'r') as file:
    line = file.readline()
    while line:
        left, right = line.split("   ")
        ids_left.append(int(left))
        ids_right.append(int(right.replace("\n", "")))
        line = file.readline()

ids_right_count = {}

for id in ids_right:
    ids_right_count[id] = ids_right_count.get(id, 0) + 1

res = 0

for id in ids_left:
    if id in ids_right_count:
        res += id * ids_right_count[id]

print(res)