# Terrible terrible terrible terrible terrible terrible
dependencies2 = {}
dependencies1 = {}  
input_arrs = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line and line != "\n":
        num1, num2 = line.split("|")
        num1 = int(num1)
        num2 = int(num2)
        if num1 not in dependencies1:
            dependencies1[num1] = set()
        if num2 not in dependencies1:
            dependencies1[num2] = set()
        if num1 not in dependencies2:
            dependencies2[num1] = set()
        if num2 not in dependencies2:
            dependencies2[num2] = set()
        dependencies1[num2].add(num1)
        dependencies2[num1].add(num2)
        line = file.readline()
    
    line = file.readline()
    while line:
        arr = line.split(",")
        arr = [int(i) for i in arr]
        input_arrs.append(arr)
        line = file.readline()

def check_arr(arr):
    visited = set()
    for i in arr:
        for d in dependencies2[i]:
            if d in visited:
                return False
        visited.add(i)
    return True

inc_arrs = []
for arr in input_arrs:
    visited = set()
    not_found = False
    if not check_arr(arr):
        inc_arrs.append(arr)

res = 0

for arr in inc_arrs:
    nums_used = set()
    latest_num = -1
    nums_in_arr = set(arr.copy())
    while len(nums_used) <= len(arr) // 2:
        possible_nums = []
        for i in arr:
            if i in nums_used:
                continue
            combined = nums_in_arr.union(dependencies1[i])
            if len(combined) == len(nums_in_arr) + len(dependencies1[i]):
                nums_used.add(i)
                nums_in_arr.remove(i)
                latest_num = i
                break
    res += latest_num

print(res)
    

