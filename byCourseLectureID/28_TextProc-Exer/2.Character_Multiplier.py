imp_line = input().split(" ")
total = 0
str1 = imp_line[0]
str2 = imp_line[1]
str3 = ''
if len(str1) > len(str2):
    diff = len(str1) - len(str2)
    str3 = str1[len(str1)-diff:]
    str1 = str1[:len(str1)-diff]
elif len(str1) < len(str2):
    diff = len(str2) - len(str1)
    str3 = str2[len(str2)-diff:]
    str2 = str2[:len(str2)-diff]
if len(str1) == len(str2):
    for i in range(0, len(str1)):
        total = total + (ord(str1[i]) * ord(str2[i]))
if str3 != '':
    for ch in str3:
        total = total + ord(ch)
print(total)
