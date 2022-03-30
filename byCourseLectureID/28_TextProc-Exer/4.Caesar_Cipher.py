imp_line = input()
encrypted_ver = ''
for ch in imp_line:
    encrypted_ver = encrypted_ver + chr(ord(ch) + 3)
print(encrypted_ver)
