import re
thislist = []
while True:
    try:
        names = input()
    except EOFError:
        break
    matches = re.findall(r"\d+", names)
    thislist.extend(matches)
print(" ".join(thislist))
