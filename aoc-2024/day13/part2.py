import math
arr_A = []
arr_B = []
prizes = []

with open("input.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    temp = file.readline()
    while line1:
        in1, in2 = line1.split(",")
        arr_A.append((int(in1.split("+")[1]), int(in2.split("+")[1])))
        in1, in2 = line2.split(",")
        arr_B.append((int(in1.split("+")[1]), int(in2.split("+")[1])))
        in1, in2 = line3.split(",")
        prizes.append((int(in1.split("=")[1]), int(in2.split("=")[1])))
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        temp = file.readline()


res = 0

prizes = [(10000000000000 + i, 10000000000000 + j) for (i, j) in prizes]

for i in range(len(prizes)):
    prize_x, prize_y = prizes[i]
    a_x, a_y = arr_A[i]
    b_x, b_y = arr_B[i]
    if prize_x % (math.gcd(a_x, b_x)) != 0 or prize_y % (math.gcd(a_y, b_y)) != 0:
        continue
    
    # 94a + 22b = 8400
    # 34a + 67b = 5400
    # a = (5400 - 67b) / 34
    # 94 * (5400 - 67b) / 34 + 22b = 8400
    # 22b - (94 * 67)b / 34 = 8400 - (5400 / 34) * 94
    # (34 * 22)b - (94 * 67)b = 8400 * 34 - 5400 * 94
    # b = (8400 * 34 - 5400 * 94) / (34 * 22 - 94 * 67)

    b = (prize_x * a_y - prize_y * a_x) // (a_y * b_x - a_x * b_y)
    a = (prize_x - b_x * b) // a_x
    if a * a_x + b * b_x == prize_x and a * a_y + b * b_y == prize_y:
        res += 3 * a + b
    
    

print(res)



