imp_line = input().split(", ")
ok_pazzwords = list()
for pazzword in imp_line:
    correct_chars, invalchars = 0, 0
    if 3 <= len(pazzword) <= 16:
        lenisfine = True
        for ch in pazzword:
            if ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_":
                correct_chars += 1
            else:
                invalchars += 1
    if invalchars == 0 and correct_chars == len(pazzword):
        ok_pazzwords.append(pazzword)
print(*ok_pazzwords, sep="\n")
