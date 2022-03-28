from collections import Counter
my_dict = dict(Counter(input()))
for key, value in my_dict.items():
    if key != ' ':
        print(key, '->', value)
