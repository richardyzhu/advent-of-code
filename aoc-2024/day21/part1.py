
arr = []
with open("input.txt", "r") as file:
    line = file.readline().replace("\n", "")
    while line:
        arr.append(line)
        line = file.readline().replace("\n", "")

print(arr)

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
    else:
        cur_letter = 'A'
        for letter in code:
            dx = keypad2_coords[letter][0] - keypad2_coords[cur_letter][0]
            dy = keypad2_coords[letter][1] - keypad2_coords[cur_letter][1]
            if cur_letter == '<':
                # move y first
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
            elif letter == '<':
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
                
# v<<A>>^AvA^Av<<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
res = 0
for code in arr:
    code1 = get_sequence(keypad1, code)
    code2 = get_sequence(keypad2, code1)
    code3 = get_sequence(keypad2, code2)
    num = int(code[:len(code) - 1])
    res += num * len(code3)
    print(len(code3))
    print(code, code3)
print(res)