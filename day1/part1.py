import heapq

ids_left = []
ids_right = []

with open('input.txt', 'r') as file:
    line = file.readline()
    while line:
        left, right = line.split("   ")
        ids_left.append(int(left))
        ids_right.append(int(right.replace("\n", "")))
        line = file.readline()

heapq.heapify(ids_left)
heapq.heapify(ids_right)

res = 0

while ids_left:
    left_id = heapq.heappop(ids_left)
    right_id = heapq.heappop(ids_right)
    res += (abs(right_id - left_id))

print(res)