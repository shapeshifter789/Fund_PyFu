import re
mylist = []
input_line = input()
matches = re.findall(r"(?<=\b_)[a-zA-Z0-9]+\b", input_line)
print(",".join(matches))
