

with open("test_input2.txt", "r") as file:
    line = file.readline().replace("\n", "")
    a = int(line.split(" ")[-1])
    line = file.readline().replace("\n", "")
    b = int(line.split(" ")[-1])
    line = file.readline().replace("\n", "")
    c = int(line.split(" ")[-1])
    line = file.readline().replace("\n", "")
    line = file.readline().replace("\n", "")
    line = line.split(" ")[-1]
    arr = line.split(",")
    arr = [int(i) for i in arr]

output = []

def get_combo_val(num):
    if num < 4:
        return num
    
    if num == 4:
        return a
    elif num == 5:
        return b
    elif num == 6:
        return c

print(arr)
pointer = 0
while True:
    if pointer >= len(arr):
        break
    op = arr[pointer]
    combo = arr[pointer + 1]

    if op == 0:
        a = a // (2**get_combo_val(combo))
    elif op == 1:
        b = b ^ combo
    elif op == 2:
        b = get_combo_val(combo) % 8
    elif op == 3:
        if a != 0:
            pointer = combo
        else:
            pointer += 2
    elif op == 4:
        b = b ^ c
    elif op == 5:
        output.append(get_combo_val(combo) % 8)
    elif op == 6:
        b = a // (2**get_combo_val(combo))
    elif op == 7:
        c = a // (2**get_combo_val(combo))
    
    if op != 3:
        pointer += 2

print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")
print(",".join([str(i) for i in output]))