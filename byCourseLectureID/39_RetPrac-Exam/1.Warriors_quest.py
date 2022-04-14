string_imp = input()
commands = input()
while commands != "For Azeroth":
    if commands == "GladiatorStance":
        string_imp = string_imp.upper()
        print(string_imp)
    elif commands == "DefensiveStance":
        string_imp = string_imp.lower()
        print(string_imp)
    elif "Dispel" in commands:
        index = int(commands.split(" ")[1])
        letter = commands.split(" ")[2]
        if len(string_imp) >= index >= 0:
            string_imp = string_imp.replace(string_imp[index], letter, 1)
            print("Success!")
        elif len(string_imp) < index or index < 0:
            print("Dispel too weak.")
    elif "Target Change" in commands:
        fir_str = commands.split(" ")[2]
        sec_str = commands.split(" ")[3]
        if fir_str in string_imp:
            string_imp = string_imp.replace(fir_str, sec_str)
            print(f'{string_imp}')
        elif fir_str not in string_imp:
            print(f'{string_imp}')
    elif "Target Remove" in commands:
        fir_str1 = commands.split(" ")[2]
        if fir_str1 in string_imp:
            string_imp = string_imp.replace(fir_str1, '')
            print(f'{string_imp}')
        elif fir_str1 not in string_imp:
            pass
    else:
        print(f"Command doesn't exist!")
    commands = input()
