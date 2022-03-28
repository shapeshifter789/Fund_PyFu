countries = input().split(", ")
capitals = input().split(", ")
countries_n_capitals = {countries[i]: capitals[i] for i in range(len(countries)) for i in range(len(capitals))}
for key, value in countries_n_capitals.items():
    print(key, '->', value)
