
arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        arr.append(int(line))
        line = file.readline().replace("\n", "")

res = 0

def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num % 16777216

for num in arr:
    for i in range(2000):
        num_temp = num * 64
        num = mix(num, num_temp)
        num = prune(num)
        num_temp = num // 32
        num = mix(num, num_temp)
        num = prune(num)
        num_temp = num * 2048
        num = mix(num, num_temp)
        num = prune(num)
    res += num

print(res)