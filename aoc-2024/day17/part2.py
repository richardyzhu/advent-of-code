

with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    input_a = int(line.split(" ")[-1])
    line = file.readline().replace("\n", "")
    b = int(line.split(" ")[-1])
    line = file.readline().replace("\n", "")
    c = int(line.split(" ")[-1])
    line = file.readline().replace("\n", "")
    line = file.readline().replace("\n", "")
    line = line.split(" ")[-1]
    arr = line.split(",")
    arr = [int(i) for i in arr]


def check_val(n, index):
    a = n
    b = 0
    c = 0
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
    
    for i in range(-index, 0, 1):
        if output[i] != arr[i]:
            return False
    return True
    

# Program: 2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0

# B = A % 8
# B = B ^ 5
# C = A // 2**B
# A = A // 8
# B = B ^ C
# B = B ^ 6
# Output B
# Repeat if A not 0

test = 0
index = 1
for i in range(len(arr) - 1, -1, -1):
    test = test * 8
    while True:
        if check_val(test, index):
            index += 1
            break
        test += 1

    print(f"Num {test} found for index {i}")


