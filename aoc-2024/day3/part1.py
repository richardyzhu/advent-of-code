

with open("input.txt", "r") as file:
    input_str = file.read()

i = 0
res = 0

# is this the worst code of all time
while i < len(input_str) - 7:
    if input_str[i:i+4] == "mul(":
        for j in range(7, 4, -1):
            if input_str[i+4:i+j].isnumeric():
                if input_str[i+j] == ",":
                    for k in range(j+4, j+1, -1):
                        if input_str[i+j+1:i+k].isnumeric():
                            if input_str[i+k] == ")":
                                num1 = int(input_str[i+4:i+j])
                                num2 = int(input_str[i+j+1:i+k])
                                print(input_str[i:i+k+1])
                                res += num1 * num2
                            break
                break
    i += 1

print(res)
