import sqlite3

conn = sqlite3.connect("PhoneBook_DB.db")
cur = conn.cursor()

def create_tb():
    cur.execute("create table if not exists phone_book (id text, name text, email text, contact_no text, h_contact_no text)")
    conn.commit()

    print("Table has been created successfully...")

# create_tb()

def show_data():
    cur.execute("select * from phone_book")
    print(cur.fetchall())

show_data()