# To initialise this, run the function create_table() first, and then run the regular code.


import sqlite3

import time
import serial

# ser = serial.Serial('COM7', 9600)
# ser.flush()

try:
    ser = serial.Serial('COM7', 9600) #check the port number for your device
    ser.flush()
except:
    ser=serial.Serial()


# Item_Id, Item_Name, Compartment, X_Pos, Height, Stock

ERROR_TUPLE = (-1, -1, -1, -1, -1, -1)


def create_table():
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS TEST1")

    sql = '''CREATE TABLE TEST1(
       Item_ID INT NOT NULL,
       Item_Name CHAR(1000),
       Compartment CHAR(100),
       X_Pos INT,
       Height INT,
       Stock INT
    )'''
    cursor.execute(sql)
    print("Table created successfully........")

    conn.commit()

    conn.close()


def get_all_locations_of_item(item_id):
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    get_data = '''SELECT Item_ID, Item_Name, Compartment, X_Pos, Height, Stock
                FROM TEST1
                WHERE Item_ID= '''
    get_data = get_data + str(item_id)

    cursor.execute(get_data)
    output = cursor.fetchall()

    conn.commit()

    conn.close()

    return output

def get_list_of_items():
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    get_data = '''SELECT Item_ID, Item_Name
    FROM TEST1'''

    cursor.execute(get_data)
    output=cursor.fetchall()

    conn.commit()

    conn.close()

    return output


# only gets non-zero stock item
def get_item(item_id):
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    get_data = '''SELECT Item_ID, Item_Name, Compartment, X_Pos, Height, Stock
                FROM TEST1
                WHERE Item_ID= '''
    get_data = get_data + str(item_id)
    get_data = get_data + " AND Stock > "
    get_data = get_data + str(0)

    cursor.execute(get_data)
    output = cursor.fetchall()

    conn.commit()

    conn.close()

    if len(output) > 0:
        return output[0]  # optimise output
    else:
        return ERROR_TUPLE


def drop_item(item_id, item_name, compartment, x_pos, height, stock):
    if stock > 0:
        conn = sqlite3.connect('sqlite_test.db')
        cursor = conn.cursor()

        # motor function to drop item
        if item_id==1:
            time.sleep(1)
            try:
                ser.write(b'A')
            except:
                print("Port is not open. If it was, item would drop")

        else:
            time.sleep(1)
            try:
                ser.write(b'B')
            except:
                print("Port is not open. If it was, the item would drop")

        update_item = '''UPDATE TEST1
                    SET Stock='''
        update_item = update_item + str(stock - 1)
        update_item = update_item + '''
                                WHERE Item_ID= '''
        update_item = update_item + str(item_id)
        update_item = update_item + ''' AND Item_Name= "'''
        update_item = update_item + item_name
        update_item = update_item + '''" AND Compartment= "'''
        update_item = update_item + compartment
        update_item = update_item + '''" AND X_Pos= '''
        update_item = update_item + str(x_pos)
        update_item = update_item + ''' AND Height= '''
        update_item = update_item + str(height)

        cursor.execute(update_item)

        conn.commit()

        conn.close()


def fetch_item(tup):
    if tup == ERROR_TUPLE:
        print("Stock of item is over, or item does not exist")

    else:

        item_id = tup[0]
        item_name = tup[1]
        compartment = tup[2]
        x_pos = tup[3]
        height = tup[4]
        stock = tup[5]

        drop_item(item_id, item_name, compartment, x_pos, height, stock)


def delete_item(item_id, item_name, compartment, x_pos, height, stock):
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    delete_item = '''DELETE FROM TEST1 WHERE Item_ID= '''
    delete_item = delete_item + str(item_id)
    delete_item = delete_item + ''' AND Item_Name= "'''
    delete_item = delete_item + item_name
    delete_item = delete_item + '''" AND Compartment= "'''
    delete_item = delete_item + compartment
    delete_item = delete_item + '''" AND X_Pos= '''
    delete_item = delete_item + str(x_pos)
    delete_item = delete_item + ''' AND Height= '''
    delete_item = delete_item + str(height)
    delete_item = delete_item + ''' AND Stock= '''
    delete_item = delete_item + str(stock)

    cursor.execute(delete_item)

    conn.commit()

    conn.close()


def add_new_item(item_id, item_name, compartment, x_pos, height, stock):
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    search_for_item_occupied = '''SELECT * FROM TEST1 WHERE Compartment= "'''
    search_for_item_occupied = search_for_item_occupied + str(compartment)
    search_for_item_occupied = search_for_item_occupied + '''" AND X_Pos= '''
    search_for_item_occupied = search_for_item_occupied + str(x_pos)
    search_for_item_occupied = search_for_item_occupied + ''' AND Height= '''
    search_for_item_occupied = search_for_item_occupied + str(height)

    cursor.execute(search_for_item_occupied)

    output = cursor.fetchall()

    if len(output) > 0:
        print("Already Occupied")
    else:
        insert_item = '''INSERT INTO TEST1 (Item_ID,Item_Name,Compartment,X_Pos,Height,Stock)
                       VALUES ('''

        insert_item = insert_item + str(item_id) + ", '"
        insert_item = insert_item + item_name + "', "
        insert_item = insert_item + "'" + compartment + "', "
        insert_item = insert_item + str(x_pos) + ", "
        insert_item = insert_item + str(height) + ", "
        insert_item = insert_item + str(stock) + " )"

        cursor.execute(insert_item)

    conn.commit()

    conn.close()


def add_stock_to_item(item_id, item_name, compartment, x_pos, height, stock, added_stock):
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    update_item = '''UPDATE TEST1
                SET Stock='''
    update_item = update_item + str(stock + added_stock)
    update_item = update_item + '''
                            WHERE Item_ID= '''
    update_item = update_item + str(item_id)
    update_item = update_item + ''' AND Item_Name= "'''
    update_item = update_item + item_name
    update_item = update_item + '''" AND Compartment= "'''
    update_item = update_item + compartment
    update_item = update_item + '''" AND X_Pos= '''
    update_item = update_item + str(x_pos)
    update_item = update_item + ''' AND Height= '''
    update_item = update_item + str(height)

    cursor.execute(update_item)

    conn.commit()

    conn.close()


def set_stock_for_item(item_id, item_name, compartment, x_pos, height, stock, new_stock):
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    update_item = '''UPDATE TEST1
                SET Stock='''
    update_item = update_item + str(new_stock)
    update_item = update_item + '''
                            WHERE Item_ID= '''
    update_item = update_item + str(item_id)
    update_item = update_item + ''' AND Item_Name= "'''
    update_item = update_item + item_name
    update_item = update_item + '''" AND Compartment= "'''
    update_item = update_item + compartment
    update_item = update_item + '''" AND X_Pos= '''
    update_item = update_item + str(x_pos)
    update_item = update_item + ''' AND Height= '''
    update_item = update_item + str(height)

    cursor.execute(update_item)

    conn.commit()

    conn.close()


def clear_table():
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    clear_table = "DELETE FROM TEST1"

    cursor.execute(clear_table)

    conn.commit()

    conn.close()


def print_table():
    conn = sqlite3.connect('sqlite_test.db')
    cursor = conn.cursor()

    get_table = "SELECT * FROM TEST1"

    cursor.execute(get_table)

    output = cursor.fetchall()

    print("Item_ID, Item_Name, Compartment, X_Pos, Height, Stock")
    for row in output:
        print(row)


def test_add_table():
    clear_table()
    add_new_item(1, "apple", "A", 1, 1, 2)
    add_new_item(1, "apple", "A", 1, 2, 2)
    add_new_item(1, "apple", "A", 2, 1, 1)
    add_new_item(1, "apple", "A", 2, 2, 1)
    add_new_item(2, "banana", "B", 1, 1, 2)
    add_new_item(2, "banana", "B", 1, 2, 2)
    add_new_item(3, "orange", "B", 2, 1, 3)
    add_new_item(3, "orange", "B", 2, 2, 1)
