from functools import cache

arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    arr = [int(i) for i in line.split(" ")]



def check_digits(n):
    counter = 0
    while n > 0:
        counter += 1
        n = n // 10
    return counter

def get_nums(n, digits):
    right_num = 0
    half = digits // 2
    mult_factor = 1
    for i in range(half):
        right_num += mult_factor * (n % 10)
        n = n // 10
        mult_factor *= 10
    return n, right_num


@cache
def recurse(num, iters):
    if iters == 75:
        return 1
    
    if num == 0:
        return recurse(1, iters + 1)

    num_digits = check_digits(num)

    if num_digits % 2 == 1:
        return recurse(num * 2024, iters + 1)
    else:
        left, right = get_nums(num, num_digits)
        return recurse(left, iters + 1) + recurse(right, iters + 1)

res = 0
for num in arr:
    res += recurse(num, 0)

print(res)
