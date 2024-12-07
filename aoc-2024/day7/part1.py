

targets = []
nums = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        targets.append(int(line.split(":")[0]))
        nums.append([int(i) for i in line.split(":")[1].replace("\n", "")[1:].split(" ")])
        line = file.readline()


res = 0
for i in range(len(targets)):
    target = targets[i]
    product = nums[i][0]
    for j in range(1, len(nums[i])):
        product *= nums[i][j]

    iter_num = 0
    while iter_num <= 2 ** (len(nums[i]) - 1):
        bits_num = iter_num
        cur_res = nums[i][0]
        for j in range(1, len(nums[i])):
            if bits_num & 1:
                cur_res *= nums[i][j]
            else:
                cur_res += nums[i][j]
            bits_num >>= 1
        if cur_res == target:
            res += target
            break
        iter_num += 1

print(res)