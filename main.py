import sqlite3
import pandas as pd
from tabulate import tabulate
from datetime import datetime
import matplotlib.pyplot as plt


def edit_staff():
    global sales_staff
    y = int(input("\nEnter - \n1-Add Staff\n2-Remove Staff"))
    if y == 1:
        sales_staff = sales_staff.append({'username': input(
            "Enter username of new staff member - "), 'password': input("Enter password of new staff member- ")}, ignore_index=True)
        print("\nNew Staff member added.")
    elif y == 2:
        del_staff = input("Enter username of staff member to be removed - ")
        if del_staff in sales_staff['username'].to_numpy():
            sales_staff.drop(
                sales_staff.loc[sales_staff['username'] == del_staff].index, inplace=True)
            print('Staff member removed.')
        else:
            print('No staff with given username found in database.')


def view_sales_report():
    new_df = purchase_history['id'].value_counts().reset_index()
    new_df.columns = ['id', 'freq']
    new_df = new_df.merge(df, left_on='id', right_on='item_ID').head(5)
    fig, ax = plt.subplots(figsize=(6, 4))
    plt.bar(new_df['item_name'], new_df['freq'], width=0.3)
    plt.xlabel('Product Names', fontweight='bold', alpha=0.5)
    plt.ylabel('Frequency', fontweight='bold', alpha=0.5)
    plt.title("Top 5 Selling Products", fontweight='bold', alpha=0.5)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    plt.tick_params(axis='both', which='both', bottom=False, left=False)
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()


def edit_inventory():
    global df
    x = int(input("\nEnter - \n1-Add Item\n2-Remove Item\n3-Edit Item"))
    if x == 1:
        new_id = df['item_ID'].to_numpy()[-1]
        new_id += 1
        df = df.append({'item_ID': new_id, 'item_name': input("Enter product name - "), 'price': int(input("Enter product price - ")),
                        'quantity': int(input("Enter product quantity - ")), 'category': input("Enter product category - ")}, ignore_index=True)
        print("\nItem added to inventory.")
    elif x == 2:
        del_id = int(input("Enter id of item to be removed - "))
        if del_id in df['item_ID'].to_numpy():
            df.drop(df.loc[df['item_ID'] == del_id].index, inplace=True)
            print("\nProduct removed from inventory.")
        else:
            print("\nItem with given id not found in inventory.")
    elif x == 3:
        edit_id = int(input("Enter id of item to be edited - "))
        if edit_id in df['item_ID'].to_numpy():
            df.loc[df['item_ID'] == edit_id, ['item_name', 'price', 'quantity', 'category']] = [input(
                'Enter new item name - '), int(input("Enter new price - ")), int(input("Enter new quantity")), input("Enter product category - ")]
            print("\nItem updated.")


def return_item():
    rn = retrieve_old_transaction()
    if not rn:
        return
    ir = input("Proceed to return? (Y/N)")
    if ir == 'Y' or ir == 'y':
        df.loc[df['item_ID'] == int(rn[:4]), 'quantity'] += 1
        print('\nItem returned successfully. Refund initiated.')


def select_user():
    u = input("Enter username - ")
    try:
        try:
            if sales_staff[sales_staff['username'] == u]['password'].iloc[0] == input("Enter password - "):
                return 1
            else:
                print("Invalid credentials")
        except:
            if admin[admin['username'] == u]['password'].iloc[0] == input("Enter password - "):
                return 2
            else:
                print("Invalid credentials")

    except:
        print("User not found")
        return


def payment(amount):
    print("\nRedirecting to payment interface...")
    return True


def generate_receipt(purchased_items):
    global purchase_history
    print("Item ID \t Receipt Number")
    for i in purchased_items:
        temp_receipt = datetime.now().strftime(str(i) + "%d%m%y%H%M%S")
        print(i, " \t ", temp_receipt)
        purchase_history = purchase_history.append(
            {'id': i, 'receipt_number': temp_receipt}, ignore_index=True)


def display_menu():
    return int(input("Enter choice - \n1 - Start Shopping\n2 - Buy Cart Items\n3 - Retrieve Old Transaction\n4 - Return Item\n9 - Exit"))


def display_admin_menu():
    return int(input("Enter choice - \n1 - Start Shopping\n2 - Buy Cart Items\n3 - Retrieve Old Transaction\n4 - Return Item\n5 - Add/Remove/Edit Item\n6 - View Sales Report\n7 - Add/Remove Staff\n9 - Exit"))


def display_item(sr):
    item = sr.copy()
    item.columns = ['ID', 'Name', 'Price', 'Quantity']
    print(tabulate(item, headers='keys', tablefmt='pretty'))


def retrieve_old_transaction():
    rn = input("\n\nEnter receipt number - ")
    if rn not in purchase_history['receipt_number'].values:
        print('\nTransaction not found!')
        return
    print("\nItem ID = ", rn[:4])
    print("Name of Product = ", df[df['item_ID']
                                   == int(rn[:4])]['item_name'].iloc[0])
    d = datetime.strptime(rn[4:], "%d%m%y%H%M%S")
    print("Date of Purchase = ", d.strftime("%d %b %Y"))
    return rn


def begin_transaction(df, cart):
    if not cart:
        print('\nThere are no items in cart.')
        return
    print("\n\nITEMS IN CART : ")
    n = 0
    total_bill = 0
    for i in cart:
        n += 1
        print(n, "\t\t", df[df['item_ID'] == i]['item_name'].iloc[0],
              "\t\t", df[df['item_ID'] == i]['price'].iloc[0])
        total_bill += df[df['item_ID'] == i]['price'].iloc[0]
    print("\nTotal Price = $", total_bill)

    if payment(total_bill):
        print("Payment Successful!")
        generate_receipt(cart)
        for i in cart:
            df.loc[df['item_ID'] == i, 'quantity'] -= 1
        cart = []
    else:
        print("Payment failed!")


def begin_shopping(df, cart):
    temp = input("Enter item name or id - ")
    try:
        id = int(temp)
        search_result = df[df['item_ID'] == id][[
            "item_ID", "item_name", "price", "quantity"]]
    except:
        name = temp
        search_result = df[df['item_name'].str.contains(
            name, case=False)][["item_ID", "item_name", "price", "quantity"]]
        if len(search_result) > 1:
            display_item(search_result)
            id = int(input("Enter id of the product you wish to purchase - "))
            search_result = df[df["item_ID"] == id][[
                "item_ID", "item_name", "price", "quantity"]]
    if search_result.empty:
        print("Sorry, Could not find what you were looking for.")
        return
    else:
        display_item(search_result)
    ch = int(input(
        "Press - \n1-Add current item to cart\n2-Leave item & Continue Shopping"))
    if ch == 1:
        cart.append(search_result['item_ID'].tolist()[0])
        ch1 = int(input(
            "Item Added to Cart.\n Press \n1 - To buy cart items.\n2 - To Continue Shopping "))
        if ch1 == 1:
            begin_transaction(df, cart)
        elif ch1 == 2:
            begin_shopping(df, cart)
    elif ch == 2:
        begin_shopping(df, cart)


cart = []
conn = sqlite3.connect("test.db")
df = pd.read_sql("select * from inventory;", con=conn)
sales_staff = pd.read_sql("select * from sales_staff;", con=conn)
admin = pd.read_sql("select * from admin;", con=conn)
purchase_history = pd.read_sql("select * from purchase_history", con=conn)


user = select_user()
while True:
    if user == 1:
        ch = display_menu()
        if ch == 9:
            break
        elif ch == 1:
            begin_shopping(df, cart)
        elif ch == 2:
            begin_transaction(df, cart)
        elif ch == 3:
            retrieve_old_transaction()
        elif ch == 4:
            return_item()
    elif user == 2:
        ch = display_admin_menu()
        if ch == 9:
            break
        elif ch == 1:
            begin_shopping(df, cart)
        elif ch == 2:
            begin_transaction(df, cart)
        elif ch == 3:
            retrieve_old_transaction()
        elif ch == 4:
            return_item()
        elif ch == 5:
            edit_inventory()
        elif ch == 6:
            view_sales_report()
        elif ch == 7:
            edit_staff()
    else:
        break


df.to_sql("inventory", con=conn, if_exists='replace', index = False)
sales_staff.to_sql("sales_staff", con=conn, if_exists='replace', index = False)
admin.to_sql("admin",con= conn, if_exists='replace', index = False)
purchase_history.to_sql("purchase_history",con=conn, if_exists='replace', index=False)