import sqlite3

conn = sqlite3.connect('test.db')
# conn.execute("create table inventory(item_ID int not null,item_name text not null,price int not null,quantity int not null,category text);")

# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1001, 'Champion Mens Classic Jersey', 18, 15, 'Shirts');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1002, 'Wrangler K87 Short Sleeve T-Shirt', 50, 7, 'Shirts');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1003, 'Wrangler Riggs Workwear', 30, 7, 'Shirts');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1004, 'Jerzees Mens Spotshield Polo Shirt', 15, 5, 'Shirts');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1005, 'Carhartt Mens Long Sleeve T-Shirt', 40, 3, 'Shirts');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1006, 'Fleece Hoodie',39 , 5, 'Hoodies');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1007, 'Adidas Z.N.E.',100 , 6, 'Hoodies');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1008, 'CNY Hoodie',90 , 8, 'Hoodies');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1009, 'Adidas Sportswear Stadium Pullover',65 , 3, 'Hoodies');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1010, 'R.Y.C. Graphic Hoodie',90 , 2, 'Hoodies');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1011, 'Adidas Easy Vulc 2.0', 70, 10, 'Shoes');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1012, 'Salomon Men outBACK 500', 150, 2, 'Shoes');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1013, 'Adidas Zeta 2.0', 90, 20, 'Shoes') ;")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1014, 'Nike LeBron Witness IV', 160, 5, 'Shoes');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1015, 'Babolat Propulse Rage', 95, 3, 'Shoes');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1016, 'Fossil Gen 5', 300, 4, 'Watches');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1017, 'Seiko Mens SNK809', 90, 3, 'Watches');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1018, 'Citizen Eco Drive Promaster', 150, 2, 'Watches');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1019, 'G Shock Rangeman GW', 300, 5, 'Watches');")
# conn.execute("insert into inventory (item_id, item_name, price, quantity, category) values (1020, 'Gucci SYNC XXL', 330, 5, 'Watches');")


# conn.execute("create table sales_staff(username text not null, password text not null);")
# conn.execute("insert into sales_staff (username, password) values('tony', 'stark');")
# conn.execute("insert into sales_staff (username, password) values('steve', 'rogers');")
# conn.execute("insert into sales_staff (username, password) values('bruce', 'banner');")
# conn.execute("insert into sales_staff (username, password) values('peter', 'parker');")
# conn.execute("insert into sales_staff (username, password) values('natasha', 'romanoff');")


# conn.execute("create table admin(username text not null, password text not null);")
# conn.execute("insert into admin (username, password) values('stan', 'lee');")
# conn.execute("insert into admin (username, password) values('jack', 'kirby');")

# conn.execute("create table purchase_history(id int not null, receipt_number int not null);")
#
# conn.commit()
cursor = conn.execute("select * from purchase_history")
for i in cursor.fetchall():
    print(i)
