
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

sequences = []
for num in arr:
    prev_num = num % 10
    sequences.append([])
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
        sequences[-1].append((((num % 10) - prev_num), num % 10))
        prev_num = num % 10


score_dict = {}

for sequence in sequences:
    seen = set()
    l = -1
    for i in range(4, len(sequence)):
        l += 1
        changes = []
        for j in range(l, i):
            changes.append(sequence[j][0])
        if tuple(changes) in seen:
            continue
        seen.add(tuple(changes))
        
        score_dict[tuple(changes)] = score_dict.get(tuple(changes), 0) + sequence[i - 1][1]

print(score_dict[max(score_dict, key=score_dict.get)])



