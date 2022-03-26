import re
input_line = ''
purchase_list = list()
full_match_regex = r'(>>)([a-zA-Z]+)(<<)(([0-9]+\.[0-9]+)|([0-9]+))(!)([1-9]+)'
temp_list = list()
products_list = list()
total_sum = 0
while input_line != 'Purchase':
    input_line = input()
    if input_line == 'Purchase':
        break
    if input_line != 'Purchase':
        purchase_list.append(input_line)
for item in purchase_list:
    if re.search(full_match_regex, item) is not None:
        temp_list = re.split(r'>>|<<|!', item)
        products_list.append(temp_list[1])
        total_sum = total_sum + (float(temp_list[2]) * int(temp_list[3]))
print(f'Bought furniture:')
if total_sum > 0:
    print(*products_list, sep="\n")
print(f'Total money spend: {total_sum:.2f}')
