from pprint import pprint

reports = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        line = line.replace("\n", "")
        line_arr = line.split(" ")
        line_arr = [int(i) for i in line_arr]
        reports.append(line_arr)
        line = file.readline()

unsafe = 0


# im pretty sure this is a dp problem but im too lazy so here is the brute force solution
def check_report(report):
    increasing = report[0] < report[1]
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
            return False
        if increasing and report[i] < report[i - 1]:
            return False
        if not increasing and report[i - 1] < report[i]:
            return False
    return True

for report in reports:
    if not check_report(report):
        sol_found = False
        for i in range(len(report)):
            temp = report.copy()
            temp.pop(i)
            if check_report(temp):
                sol_found = True
                break
        if not sol_found:
            unsafe += 1


res = len(reports) - unsafe
print(res)