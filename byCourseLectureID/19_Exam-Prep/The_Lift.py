imp_people = int(input())
imp_lift = input().split(" ")
imp_lift_int = [int(i) for i in imp_lift]
initial_passengers = sum(imp_lift_int)
list_1s = [1] * len(imp_lift_int)
not_full_elem_num = ((imp_people + sum(imp_lift_int)) % 4)
not_full_elems = len(imp_lift_int) - ((imp_people + sum(imp_lift_int)) // 4)
full_elems = len(imp_lift_int) - not_full_elems
first_part = [x * 4 for x in list_1s[:full_elems:]]
second_part = [not_full_elem_num for y in list_1s[full_elems:full_elems + 1:]]
third_part = [0 for z in list_1s[full_elems + 1::]]
full_list = first_part + second_part + third_part
if ((imp_people + sum(imp_lift_int)) // 4) < len(imp_lift_int):
    print(f"The lift has empty spots!")
    print(*full_list, sep=' ')
elif ((imp_people + sum(imp_lift_int)) // 4) == len(imp_lift_int) and ((imp_people + sum(imp_lift_int)) % 4) == 0:
    print(*full_list, sep=' ')
elif ((imp_people + sum(imp_lift_int)) // 4) == len(imp_lift_int) and ((imp_people + sum(imp_lift_int)) % 4) > 0:
    print(f"There isn't enough space! {imp_people - sum(full_list) + initial_passengers} people in a queue!")
    print(*full_list, sep=' ')
elif ((imp_people + sum(imp_lift_int)) // 4) > len(imp_lift_int):
    print(f"There isn't enough space! {imp_people - sum(full_list) + initial_passengers} people in a queue!")
    print(*full_list, sep=' ')
