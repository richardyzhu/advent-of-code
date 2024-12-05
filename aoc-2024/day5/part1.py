
dependencies = {}  # num -> [array of dependencies]
input_arrs = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line and line != "\n":
        num1, num2 = line.split("|")
        num1 = int(num1)
        num2 = int(num2)
        if num1 not in dependencies:
            dependencies[num1] = set()
        if num2 not in dependencies:
            dependencies[num2] = set()
        dependencies[num1].add(num2)
        line = file.readline()
    
    line = file.readline()
    while line:
        arr = line.split(",")
        arr = [int(i) for i in arr]
        input_arrs.append(arr)
        line = file.readline()

res = 0
for arr in input_arrs:
    visited = set()
    not_found = False
    for i in arr:
        for d in dependencies[i]:
            if d in visited:
                not_found = True
                break
        if not_found:
            break
        visited.add(i)
    if not not_found:
        res += arr[len(arr) // 2]

print(res)
