from database import *

while True:
    print("")
    print("")
    print('''If you want to:
Print the table, enter 1.
Find item with some item ID, enter 2.
Drop item with some item ID, enter 3.
Add new item, enter 4.
Add stock to existing item, enter 5.
Set stock for existing item, enter 6.
Delete item, enter 7.
Reset the table, enter 8.
Exit, enter 9.

''')
    try:
        choice = int(input())
        if choice == 1:
            print_table()
        if choice == 2:
            print("Enter item ID")
            item_id = int(input())
            print(get_item(item_id))
        if choice == 3:
            print("Enter item ID")
            item_id = int(input())
            fetch_item(get_item(item_id))
            print("Item dropped")
        if choice == 4:
            print(
                "Enter the item ID, item name, compartment, x position, height, stock, of the added item. Make sure each field is space-separated.")
            (item_id, item_name, compartment, x_pos, height, stock) = map(str, input().split(' '))
            item_id = int(item_id)
            x_pos = int(x_pos)
            height = int(height)
            stock = int(stock)
            add_new_item(item_id, item_name, compartment, x_pos, height, stock)
            print("Item added")
        if choice == 5:
            print(
                "Enter the item ID, item name, compartment, x position, height, stock, added stock, of the replenished item. Make sure each field is space-separated.")
            (item_id, item_name, compartment, x_pos, height, stock, added_stock) = map(str, input().split(' '))
            item_id = int(item_id)
            x_pos = int(x_pos)
            height = int(height)
            stock = int(stock)
            added_stock = int(added_stock)
            add_stock_to_item(item_id, item_name, compartment, x_pos, height, stock, added_stock)
            print("Item replenished")
        if choice == 6:
            print(
                "Enter the item ID, item name, compartment, x position, height, stock, new stock, of the replenished item. Make sure each field is space-separated.")
            (item_id, item_name, compartment, x_pos, height, stock, new_stock) = map(str, input().split(' '))
            item_id = int(item_id)
            x_pos = int(x_pos)
            height = int(height)
            stock = int(stock)
            new_stock = int(new_stock)
            set_stock_for_item(item_id, item_name, compartment, x_pos, height, stock, new_stock)
            print("Item replenished")
        if choice == 7:
            print(
                "Enter the item ID, item name, compartment, x position, height, stock of the item to delete. Make sure each field is space-separated.")
            (item_id, item_name, compartment, x_pos, height, stock) = map(str, input().split(' '))
            item_id = int(item_id)
            x_pos = int(x_pos)
            height = int(height)
            stock = int(stock)
            delete_item(item_id, item_name, compartment, x_pos, height, stock)
            print("Item deleted")
        if choice == 8:
            clear_table()
        if choice == 9:
            break
    except Exception as e:
        print("There was an error as follows:")
        print(e)