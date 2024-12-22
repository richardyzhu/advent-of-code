from functools import cache
arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        arr.append(line)
        line = file.readline().replace("\n", "")

keypad1 = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['', '0', 'A']]
keypad2 = [['', '^', 'A'], ['<', 'v', '>']]

keypad1_coords = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
keypad2_coords = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}


def get_sequence(keypad, code):
    sequence = []
    if keypad[0][0] == '7':
        cur_letter = 'A'
        for letter in code:
            dx = keypad1_coords[letter][0] - keypad1_coords[cur_letter][0]
            dy = keypad1_coords[letter][1] - keypad1_coords[cur_letter][1]
            if keypad1_coords[letter][1] == 0 and keypad1_coords[cur_letter][0] == 3:
                for i in range(abs(dx)):
                    if dx < 0:
                        sequence.append('^')
                    else:
                        sequence.append('v')
                for i in range(abs(dy)):
                    if dy < 0:
                        sequence.append('<')
                    else:
                        sequence.append('>')
            elif keypad1_coords[cur_letter][1] == 0 and keypad1_coords[letter][0] == 3:
                for i in range(abs(dy)):
                    if dy < 0:
                        sequence.append('<')
                    else:
                        sequence.append('>')
                for i in range(abs(dx)):
                    if dx < 0:
                        sequence.append('^')
                    else:
                        sequence.append('v')
            elif dy < 0:
                for i in range(abs(dy)):
                    if dy < 0:
                        sequence.append('<')
                    else:
                        sequence.append('>')
                for i in range(abs(dx)):
                    if dx < 0:
                        sequence.append('^')
                    else:
                        sequence.append('v')
            else:
                for i in range(abs(dx)):
                    if dx < 0:
                        sequence.append('^')
                    else:
                        sequence.append('v')
                for i in range(abs(dy)):
                    if dy < 0:
                        sequence.append('<')
                    else:
                        sequence.append('>')
            cur_letter = letter
            sequence.append('A')
    
    return "".join(sequence)


@cache
def get_robot_sequence(depth, cur_letter, letter):

    if depth == 25:
        return 1

    dx = keypad2_coords[letter][0] - keypad2_coords[cur_letter][0]
    dy = keypad2_coords[letter][1] - keypad2_coords[cur_letter][1]
    cur_str = []
    if cur_letter == '<':
        # move y first
        for i in range(abs(dy)):
            if dy < 0:
                cur_str.append('<')
            else:
                cur_str.append('>')
        for i in range(abs(dx)):
            if dx < 0:
                cur_str.append('^')
            else:
                cur_str.append('v')
    elif letter == '<':
        for i in range(abs(dx)):
            if dx < 0:
                cur_str.append('^')
            else:
                cur_str.append('v')
        for i in range(abs(dy)):
            if dy < 0:
                cur_str.append('<')
            else:
                cur_str.append('>')
    elif dy < 0:
        for i in range(abs(dy)):
            if dy < 0:
                cur_str.append('<')
            else:
                cur_str.append('>')
        for i in range(abs(dx)):
            if dx < 0:
                cur_str.append('^')
            else:
                cur_str.append('v')
    else:
        for i in range(abs(dx)):
            if dx < 0:
                cur_str.append('^')
            else:
                cur_str.append('v')
        for i in range(abs(dy)):
            if dy < 0:
                cur_str.append('<')
            else:
                cur_str.append('>')

    cur_str.append('A')
    cur_str.insert(0, 'A')
    total = 0
    for i in range(len(cur_str) - 1):
        total += get_robot_sequence(depth + 1, cur_str[i], cur_str[i + 1])
    return total

                

res = 0
for code in arr:
    new_code = get_sequence(keypad1, code)
    new_code = 'A' + new_code
    total = 0
    for i in range(len(new_code) - 1):
        total += get_robot_sequence(0, new_code[i], new_code[i + 1])
    num = int(code[:len(code) - 1])
    res += num * total
print(res)