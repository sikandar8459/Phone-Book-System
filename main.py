from tkinter import *
from tkinter import ttk
# from PIL import Image, ImageTk
import tkinter.messagebox as msg
import sqlite3
import random as rd

conn = sqlite3.connect("PhoneBook_DB.db")
cur = conn.cursor()

class PhoneBookClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Book")
        self.root.geometry("450x700+200+10")
        self.root.overrideredirect(1)
        self.root.config(bg = "white")

        Label(self.root, text = "Phone Book System", font = ("times new roman", 25, "bold"), fg = "darkred", bg = "white").place(x = 12, y = 15)

        self.close_frame = LabelFrame(self.root, bd = 0, relief = RAISED, bg = "white")
        self.close_frame.place(x = 390, y = 0, width = 60, height = 60)

        self.close_img = PhotoImage(file = "Images/Icons/close_purple.png")
        self.close_img = self.close_img.subsample(10, 10)
        Button(self.close_frame, image = self.close_img, bd = 0, command = self.root.destroy, activebackground = "white", activeforeground = "red", cursor = "hand2", font = ("", 20), fg = "red", bg = "white").pack(fill = BOTH, expand = True)

        Label(self.root, text = "", font = ("times new roman", 30, "bold"), fg = "white", bg = "red").place(x = 15, y = 58, width = 200, height = 2)
        Label(self.root, text = "", font = ("times new roman", 30, "bold"), fg = "white", bg = "red").place(x = 221, y = 58, width = 30, height = 2)
        Label(self.root, text = "", font = ("times new roman", 30, "bold"), fg = "white", bg = "red").place(x = 256, y = 58, width = 20, height = 2)
        Label(self.root, text = "", font = ("times new roman", 30, "bold"), fg = "white", bg = "red").place(x = 280, y = 58, width = 10, height = 2)
        Label(self.root, text = "", font = ("times new roman", 30, "bold"), fg = "white", bg = "red").place(x = 293, y = 58, width = 5, height = 2)

        Label(self.root, text = "ID", font = ("times new roman", 17, "bold"), fg = "darkblue", bg = "white").place(x = 10, y = 100)
        Label(self.root, text = "Name", font = ("times new roman", 17, "bold"), fg = "darkblue", bg = "white").place(x = 10, y = 150)
        Label(self.root, text = "Email", font = ("times new roman", 17, "bold"), fg = "darkblue", bg = "white").place(x = 10, y = 200)
        Label(self.root, text = "Contact No", font = ("times new roman", 17, "bold"), fg = "darkblue", bg = "white").place(x = 10, y = 250)
        Label(self.root, text = "Home Contact No", font = ("times new roman", 17, "bold"), fg = "darkblue", bg = "white").place(x = 10, y = 300)

        self.id = StringVar()
        self.id.set(rd.randint(1111,9999))
        self.name = StringVar()
        self.email = StringVar()
        self.contact_no = StringVar()
        self.h_contact_no = StringVar()

        Entry(self.root, textvariable = self.id, state = "readonly", font = ("times new roman", 17, "bold"), fg = "red", bg = "white", bd = 2, relief = SUNKEN).place(x = 200, y = 100, width = 230)
        Entry(self.root, textvariable = self.name, font = ("times new roman", 17), bg = "white", bd = 2, relief = SUNKEN).place(x = 200, y = 150, width = 230)
        Entry(self.root, textvariable = self.email, font = ("times new roman", 17), bg = "white", bd = 2, relief = SUNKEN).place(x = 200, y = 200, width = 230)
        Entry(self.root, textvariable = self.contact_no, font = ("times new roman", 17), bg = "white", bd = 2, relief = SUNKEN).place(x = 200, y = 250, width = 230)
        Entry(self.root, textvariable = self.h_contact_no, font = ("times new roman", 17), bg = "white", bd = 2, relief = SUNKEN).place(x = 200, y = 300, width = 230)

        Button(self.root, cursor = "hand2", activebackground = "green", activeforeground = "white", text = "Save", command = self.save_data, fg = "white", bg = "green", font = ("times new roman", 17, "bold"), bd = 2, relief = RAISED).place(x = 10, y = 360, width = 100, height = 40)
        Button(self.root, cursor = "hand2", activebackground = "blue", activeforeground = "white", text = "Update", command = self.update_data, fg = "white", bg = "blue", font = ("times new roman", 17, "bold"), bd = 2, relief = RAISED).place(x = 120, y = 360, width = 100, height = 40)
        Button(self.root, cursor = "hand2", activebackground = "red", activeforeground = "white", text = "Delete", command = self.delete_data, fg = "white", bg = "red", font = ("times new roman", 17, "bold"), bd = 2, relief = RAISED).place(x = 230, y = 360, width = 100, height = 40)
        Button(self.root, cursor = "hand2", activebackground = "darkred", activeforeground = "white", text = "Clear", command = self.clear_data, fg = "white", bg = "darkred", font = ("times new roman", 17, "bold"), bd = 2, relief = RAISED).place(x = 340, y = 360, width = 100, height = 40)

        self.view_frame = LabelFrame(self.root, bd = 2, relief = SUNKEN, bg = "white")
        self.view_frame.place(x = 0, y = 420, relwidth = 1, height = 280)

        Label(self.view_frame, text = "View all Contact here", font = ("times new roman", 17, "bold"), fg = "white", bg = "darkblue", bd = 2, relief = RAISED).pack(fill = X)

        self.scrollx = Scrollbar(self.view_frame, orient = HORIZONTAL)
        self.scrolly = Scrollbar(self.view_frame, orient = VERTICAL)
        self.ContactTable = ttk.Treeview(self.view_frame, columns = ("id","name","email","contact_no","h_contact_no"), xscrollcommand = self.scrollx.set, yscrollcommand = self.scrolly.set)
        self.scrollx.pack(fill = X, side = BOTTOM)
        self.scrolly.pack(fill = Y, side = RIGHT)
        self.scrollx.config(command = self.ContactTable.xview)
        self.scrolly.config(command = self.ContactTable.yview)
        self.ContactTable.pack(fill = BOTH, expand = TRUE)

        self.ContactTable.heading("id", text = "ID")
        self.ContactTable.heading("name", text = "Name")
        self.ContactTable.heading("email", text = "Email")
        self.ContactTable.heading("contact_no", text = "Contact No")
        self.ContactTable.heading("h_contact_no", text = "Alternate Contact No")

        self.ContactTable["show"] = "headings"

        self.ContactTable.column("id", width = 40)
        self.ContactTable.column("name", width = 100)
        self.ContactTable.column("email", width = 180)
        self.ContactTable.column("contact_no", width = 100)
        self.ContactTable.column("h_contact_no", width = 120)

        self.ContactTable.bind("<ButtonRelease-1>", self.view_data)
        self.show_data()

    def delete_data(self):
        try:
            if self.id.get() == "" or self.name.get() == "" or self.email.get() == "" or self.contact_no.get() == "" or self.h_contact_no.get() == "":
                msg.showerror("Delete Contact Error","Please select any contact first", parent = self.root)
            else:
                update = msg.askyesno("Delete Info","Do you really want to delete ??", parent = self.root)
                if update == True:
                    query = "delete from phone_book  where id=?"
                    value = (
                                self.id.get(),
                            )
                    cur.execute(query, value)
                    conn.commit()

                    msg.showinfo("Delete Contact Success",f"ID : {self.id.get()} has been deleted successfully...", parent = self.root)
                    self.clear_data()
                    self.show_data()
                else:
                    pass
        except Exception as ex:
            msg.showerror("Exception Error",f"Error due to {ex}", parent = self.root)
            print(ex)


    def view_data(self, event):
        f = self.ContactTable.focus()
        content = (self.ContactTable.item(f))
        row = content["values"]

        self.id.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.contact_no.set(row[3])
        self.h_contact_no.set(row[4])

    def save_data(self):
        try:
            if self.id.get() == "" or self.name.get() == "" or self.email.get() == "" or self.contact_no.get() == "" or self.h_contact_no.get() == "":
                msg.showerror("Save Contact Error","All field are required", parent = self.root)
            else:
                query = "insert into phone_book values (?,?,?,?,?)"
                value = (
                            self.id.get(),
                            self.name.get(),
                            self.email.get(),
                            self.contact_no.get(),
                            self.h_contact_no.get()
                        )
                cur.execute(query, value)
                conn.commit()

                msg.showinfo("Save Contact Success",f"Name: {self.name.get()}\nContact No : {self.contact_no.get()}\nhas been saved successfully...", parent = self.root)
                self.clear_data()
                self.show_data()
        except Exception as ex:
            msg.showerror("Exception Error",f"Error due to {ex}", parent = self.root)
            print(ex)

    def update_data(self):
        try:
            if self.id.get() == "" or self.name.get() == "" or self.email.get() == "" or self.contact_no.get() == "" or self.h_contact_no.get() == "":
                msg.showerror("Update Contact Error","Please select any contact first", parent = self.root)
            else:
                update = msg.askyesno("Update Info","Do you really want to update ??", parent = self.root)
                if update == True:
                    query = "update phone_book set name=?, email=?, contact_no=?, h_contact_no=? where id=?"
                    value = (
                                self.name.get(),
                                self.email.get(),
                                self.contact_no.get(),
                                self.h_contact_no.get(),
                                self.id.get()
                            )
                    cur.execute(query, value)
                    conn.commit()

                    msg.showinfo("Update Contact Success",f"ID : {self.id.get()} has been updated successfully...", parent = self.root)
                    self.clear_data()
                    self.show_data()
                else:
                    pass
        except Exception as ex:
            msg.showerror("Exception Error",f"Error due to {ex}", parent = self.root)
            print(ex)

    def clear_data(self):
        self.id.set(rd.randint(1111,9999))
        self.name.set("")
        self.email.set("")
        self.contact_no.set("")
        self.h_contact_no.set("")

        self.show_data()

    def show_data(self):
        cur.execute("select * from phone_book")
        result = cur.fetchall()
        self.ContactTable.delete(*self.ContactTable.get_children())
        for item in result:
            self.ContactTable.insert("", END, values = item)

if __name__ == "__main__":
    root = Tk()
    obj = PhoneBookClass(root)
    root.mainloop()
