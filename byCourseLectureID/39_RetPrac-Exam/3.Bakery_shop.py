imp_line = input()
products_list = dict()
total_sold_goods = 0
print_list = list()
while imp_line != "Complete":
    command = imp_line.split(" ")[0]
    quantity = int(imp_line.split(" ")[1])
    food = imp_line.split(" ")[2]
    if command == 'Receive':
        if food not in products_list.keys() and quantity <= 0:
            pass
        elif food in products_list.keys() and quantity <= 0:
            pass
        elif food not in products_list.keys() and quantity > 0:
            products_list[food] = quantity
        elif food in products_list.keys() and quantity > 0:
            products_list[food] += quantity
    elif command == 'Sell':
        if food not in products_list.keys():
            print(f"You do not have any {food}.")
        elif food in products_list.keys() and quantity > products_list[food]:
            print(f"There aren't enough {food}. You sold the last {products_list[food]} of them.")
            total_sold_goods += products_list[food]
            del products_list[food]
        elif food in products_list.keys() and quantity < products_list[food]:
            print(f"You sold {quantity} {food}.")
            total_sold_goods += quantity
            products_list[food] -= quantity
        elif food in products_list.keys() and quantity == products_list[food]:
            total_sold_goods += quantity
            print(f"You sold {quantity} {food}.")
            del products_list[food]
    imp_line = input()
if products_list != {}:
    for key, value in products_list.items():
        print(f"{key}: {value}")
print(f"All sold: {total_sold_goods} goods")
