

targets = []
nums = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        targets.append(int(line.split(":")[0]))
        nums.append([int(i) for i in line.split(":")[1].replace("\n", "")[1:].split(" ")])
        line = file.readline()



def get_base_3(num, length):
    base3_arr = [0 for i in range(length)]
    bit_count = 0
    while bit_count < length:
        temp = num // 3
        if num == temp * 3:
            base3_arr[bit_count] = 0
        elif num == temp * 3 + 1:
            base3_arr[bit_count] = 1
        else:
            base3_arr[bit_count] = 2
        bit_count += 1
        num = temp
    return tuple(base3_arr)


def concat(num1, num2):
    new_str = str(num1) + str(num2)
    return int(new_str)


res = 0
for i in range(len(targets)):
    target = targets[i]
    product = nums[i][0]
    for j in range(1, len(nums[i])):
        product *= nums[i][j]

    iter_num = 0
    while iter_num <= 3 ** (len(nums[i]) - 1):
        base_3 = get_base_3(iter_num, len(nums[i]) - 1)
        cur_res = nums[i][0]
        for j in range(1, len(nums[i])):
            if base_3[j - 1] == 0:
                cur_res *= nums[i][j]
            elif base_3[j - 1] == 1:
                cur_res += nums[i][j]
            else:
                cur_res = concat(cur_res, nums[i][j])
        if cur_res == target:
            res += target
            break
        iter_num += 1

print(res)