
reports = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        line = line.replace("\n", "")
        reports.append(line.split(" "))
        line = file.readline()

unsafe = 0

reports = [[int(i) for i in report] for report in reports]

for report in reports:
    increasing = True
    if report[0] > report[1]:
        increasing = False
    
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
            unsafe += 1
            break
        if increasing and report[i] < report[i - 1]:
            unsafe += 1
            break
        if not increasing and report[i - 1] < report[i]:
            unsafe += 1
            break

res = len(reports) - unsafe
print(res)