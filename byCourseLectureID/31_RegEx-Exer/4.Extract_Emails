import re
first_part = r'( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'
second_part = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'
regex_pattern = rf'{first_part}@{second_part}'
input_line = input()
matches = re.finditer(regex_pattern, input_line)
for match in matches:
    print(match[0])
