
values = {}
instructions = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        arr = line.split(":")
        num = int(arr[1].strip())
        values[arr[0]] = num
        line = file.readline().replace("\n", "")

    line = file.readline().replace("\n", "")
    while line:
        arr = line.split(" ")
        instructions.append((arr[0], arr[1], arr[2], arr[4]))
        line = file.readline().replace("\n", "")


used_instructions = set()

while len(used_instructions) < len(instructions):
    for i in range(len(instructions)):
        if instructions[i] in used_instructions:
            continue
        
        bit1, op, bit2, bit3 = instructions[i]

        if bit1 in values and bit2 in values:
            used_instructions.add(instructions[i])
            if op == 'AND':
                values[bit3] = values[bit1] & values[bit2]
            elif op == 'OR':
                values[bit3] = values[bit1] | values[bit2]
            elif op == 'XOR':
                values[bit3] = values[bit1] ^ values[bit2]

z_arr = []

for i in values:
    if i[0] == 'z':
        z_arr.append((i, values[i]))

z_arr.sort()
cur_pow = 1
res = 0
for i in range(len(z_arr)):
    res += z_arr[i][1] * cur_pow
    cur_pow *= 2

print(res)