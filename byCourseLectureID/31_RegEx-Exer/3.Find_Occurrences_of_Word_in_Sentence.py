import re
mylist = []
input_line1 = input()
input_line2 = input()
matches = re.findall(rf'\b{input_line2}\b', input_line1, re.IGNORECASE)
print(len(matches))
