
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

for i in range(len(prizes)):
    prize_x, prize_y = prizes[i]
    a_x, a_y = arr_A[i]
    b_x, b_y = arr_B[i]
    cur_x, cur_y = 0, 0
    min_tokens = float("inf")
    while cur_x <= prize_x and cur_y <= prize_y:
        tokens = (cur_x // a_x) * 3
        if (prize_x - cur_x) % b_x == 0 and (prize_y - cur_y) % b_y == 0 and ((prize_x - cur_x) // b_x) * b_y == (prize_y - cur_y):
            tokens += (prize_x - cur_x) // b_x
            min_tokens = min(min_tokens, tokens)
        cur_x += a_x
        cur_y += a_y
    
    if min_tokens != float("inf"):
        res += min_tokens

print(res)



