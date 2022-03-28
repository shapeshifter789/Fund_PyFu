imp = ''
imp_list = list()
imp_dict = dict()
while imp != 'stop':
    imp = input()
    if imp != 'stop':
        imp_list.append(imp)
for i in range(0, len(imp_list), 2):
    key = imp_list[i]
    value = int(imp_list[i + 1])
    if key in imp_dict.keys():
        imp_dict[key] += value
    else:
        imp_dict[key] = value
for key, value in imp_dict.items():
    print(key, '->', value)
