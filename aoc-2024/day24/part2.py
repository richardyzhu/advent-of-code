from collections import deque
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
        instructions.append([arr[0], arr[1], arr[2], arr[4]])
        line = file.readline().replace("\n", "")

orig_values = values.copy()

def get_values(values, instructions):
    used_instructions = set()

    while len(used_instructions) < len(instructions):
        for i in range(len(instructions)):
            if tuple(instructions[i]) in used_instructions:
                continue
            
            bit1, op, bit2, bit3 = instructions[i]

            if bit1 in values and bit2 in values:
                used_instructions.add(tuple(instructions[i]))
               
                
                if bit3 == "z19":
                    values[bit3] = 1
                    continue
                if bit3 == "vwp":
                    values[bit3] = 0
                    continue

                if bit3 == "mps":
                    values[bit3] = 1
                    continue
                if bit3 == "z25":
                    values[bit3] = 0
                    continue

                if bit3 == "cqm":
                    values[bit3] = 1
                    continue
                if bit3 == "vjv":
                    values[bit3] = 0
                    continue

                if bit3 == "vcv":
                    values[bit3] = 1
                    continue
                if bit3 == "z13":
                    values[bit3] = 0
                    continue


# cqm,pqn,qkk,vbw,vjv,vwp,z19,z25

# cqm,mqj,qkk,vbw,vjv,vwp,z19,z25

                if op == 'AND':
                    values[bit3] = values[bit1] & values[bit2]
                elif op == 'OR':
                    values[bit3] = values[bit1] | values[bit2]
                elif op == 'XOR':
                    values[bit3] = values[bit1] ^ values[bit2]
    return values


swaps = ["z19", "vwp", "mps", "z25", "cqm", "vjv", "vcv", "z13"]
print(",".join(sorted(swaps)))

values = get_values(orig_values, instructions)
z_arr = []
y_arr = []
x_arr = []

for i in values:
    if i[0] == 'z':
        z_arr.append((i, values[i]))
    if i[0] == 'x':
        x_arr.append((i, values[i]))
    if i[0] == 'y':
        y_arr.append((i, values[i]))

z_arr.sort()

def get_z_num(values):
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

    return res

x_num = 0
y_num = 0
z_num = get_z_num(values)

cur_pow = 1
for i in range(len(x_arr)):
    x_num += x_arr[i][1] * cur_pow
    cur_pow *= 2

cur_pow = 1
for i in range(len(x_arr)):
    y_num += y_arr[i][1] * cur_pow
    cur_pow *= 2

total = x_num + y_num
print(f"Total: {total}")

total_bin = str(bin(total).replace("0b", ""))
z_bin = str(bin(z_num).replace("0b", ""))
print(total_bin)
print(z_bin)
diff_indices = []

for i in range(len(total_bin)):
    if total_bin[i] != z_bin[i]:
        diff_indices.append(i)


print(diff_indices)

# dep_arr = []
# def dfs(bit):
#     if bit[0] == 'x' or bit[0] == 'y':
#         return

#     for instruction in instructions:
#         if instruction[3] == bit:
#             dep_arr.append(instruction)
#             dfs(instruction[0])
#             dfs(instruction[2])

# dfs("z26")
for instruction in instructions:
    if instruction[3][0] == 'z' and instruction[1] != 'XOR':
        print(instruction)
        print(values[instruction[3]])


def pprint(bit, max_depth=5, depth=0):
    if depth > max_depth:
        return
    if bit[0] == 'x' or bit[0] == 'y':
        print("    "*depth + bit)
    else:
        a = b = op = None
        for instruction in instructions:
            if instruction[3] == bit:
                a, op, b, _ = instruction
                break
        print("    "*depth + bit + f" = {op} {a} {b}")
        pprint(a, max_depth, depth + 1)
        pprint(b, max_depth, depth + 1)

# pprint("z45")


# pprint("z14")
# pprint("z13")
# pprint("z12")
# print(values["jpk"])



# pprint("z05")
# pprint("z04")
# pprint("z03")
# # pprint("z02")
# print("bruh")
# # print(values["z13"])
# # print(values["tnf"])
# # values["z13"], values["tnf"] = values["tnf"], values["z13"]
# # z_num = get_z_num(values)

# pprint("z26")
# pprint("z25")
# pprint("z24")
# print(values["pqn"])
# print(values["vbw"])
# pprint("z19")
# pprint("z18")
# pprint("z20")
# print(values["vwp"])
# print(values["z19"])

# pprint("z34")
# pprint("z33")
# pprint("z32")
# # pprint("z31")
# # pprint("z30")

# print(values["cqm"])
# print(values["vjv"])

pprint("z24")
pprint("z25")
pprint("z26")
# print(values["qkk"])


# pprint("z12")
# pprint("z13")
# pprint("z14")
# print(values["kpj"])

# print(dep_arr)
# temp = set()
# for dep in dep_arr:
#     if (dep[0][0] == 'x' or dep[0][0] == 'y') and dep[0] not in temp:
#         temp.add(dep[0])
#     if (dep[2][0] == 'x' or dep[2][0] == 'y') and dep[2] not in temp:
#         temp.add(dep[0])

# print(temp)

# dep_arrs = []
# for idx in diff_indices:
#     bit = 'z' + str(idx)
#     dep_arr = [bit]
#     q = deque()
#     q.append(bit)
#     while q:
#         for j in range(len(q)):
#             bit = q.popleft()
#             for i in range(len(instructions)):
#                 if instructions[i][3] == bit:
#                     dep_arr.append(instructions[i][0])
#                     dep_arr.append(instructions[i][2])
#                     q.append(instructions[i][0])
#                     q.append(instructions[i][2])
#     dep_arrs.append(dep_arr)


# dep_set = set(dep_arrs[0])

# for i in range(len(dep_arrs)):
#     dep_set = dep_set.union(dep_arrs[i])

# new_dep_set = set()
# for bit in dep_set:
#     if bit[0] == "x" or bit[0] == "y":
#         continue
#     new_dep_set.add(bit)


# dep_set_ones = []
# dep_set_zeroes = []
# for bit in new_dep_set:
#     if values[bit] == 0:
#         dep_set_zeroes.append(bit)
#     elif values[bit] == 1:
#         dep_set_ones.append(bit)

# print(dep_set_zeroes)
# print(dep_set_ones)

# for i in range(len(dep_set_zeroes) - 3):
#     for j in range(i + 1, len(dep_set_zeroes) - 2):
#         for k in range(j + 1, len(dep_set_zeroes) - 1):
#             for l in range(k + 1, len(dep_set_zeroes)):
#                 for a in range(len(dep_set_ones) - 3):
#                     for b in range(a + 1, len(dep_set_ones) - 2):
#                         for c in range(b + 1, len(dep_set_ones) - 1):
#                             for d in range(c + 1, len(dep_set_ones)):
#                                 new_values = orig_values.copy()
#                                 used_instructions = set()
#                                 while len(used_instructions) < len(instructions):
#                                     for ins in range(len(instructions)):
#                                         if instructions[ins] in used_instructions:
#                                             continue
                                        
#                                         bit1, op, bit2, bit3 = instructions[ins]

#                                         if bit1 in new_values and bit2 in new_values:
#                                             used_instructions.add(instructions[ins])
#                                             if bit3 == dep_set_zeroes[i] or bit3 == dep_set_zeroes[j] or bit3 == dep_set_zeroes[k] or bit3 == dep_set_zeroes[l]:
#                                                 new_values[bit3] = 1
#                                                 continue
#                                             if bit3 == dep_set_ones[a] or bit3 == dep_set_ones[b] or bit3 == dep_set_ones[c] or bit3 == dep_set_ones[d]:
#                                                 new_values[bit3] = 0
#                                                 continue
#                                             if op == 'AND':
#                                                 new_values[bit3] = new_values[bit1] & new_values[bit2]
#                                             elif op == 'OR':
#                                                 new_values[bit3] = new_values[bit1] | new_values[bit2]
#                                             elif op == 'XOR':
#                                                 new_values[bit3] = new_values[bit1] ^ new_values[bit2]
#                                 z_arr = []
#                                 for idx in new_values:
#                                     if idx[0] == 'z':
#                                         z_arr.append((idx, new_values[idx]))
#                                 z_arr.sort()
#                                 cur_pow = 1
#                                 res = 0
#                                 for idx in range(len(z_arr)):
#                                     res += z_arr[idx][1] * cur_pow
#                                     cur_pow *= 2
#                                 print(f"Using: {i, j, k, l} of zeroes, {a, b, c, d} of ones")
#                                 print(res)
#                                 if res == total:
#                                     print(dep_set_zeroes[i], dep_set_zeroes[j], dep_set_zeroes[k], dep_set_zeroes[l], dep_set_ones[a], dep_set_ones[b], dep_set_ones[c], dep_set_ones[d])
#                                     import sys
#                                     sys.exit()
                                
