from tkinter import Tk, Label, Entry, StringVar, Listbox, Scrollbar, Button
from database import MyDataBase


class Database_GUI(MyDataBase):

    def __init__(self, db_name):
        self.db_name = db_name
        self.window = Tk()
        super().__init__(db_name)

        self.title_label = Label(self.window, text="Title")
        self.title_label.grid(row=0, column=0)

        self.year_label = Label(self.window, text="Year")
        self.year_label.grid(row=1, column=0)

        self.author_label = Label(self.window, text="Author")
        self.author_label.grid(row=0, column=2)

        self.isbn_label = Label(self.window, text="ISBN")
        self.isbn_label.grid(row=1, column=2)

        self.title_entry = StringVar()
        self.title_text_entry = Entry(self.window, textvariable=self.title_entry)
        self.title_text_entry.grid(row=0, column=1)

        self.author_entry = StringVar()
        self.author_text_entry = Entry(self.window, textvariable=self.author_entry)
        self.author_text_entry.grid(row=0, column=3)

        self.year_entry = StringVar()
        self.year_text_entry = Entry(self.window, textvariable=self.year_entry)
        self.year_text_entry.grid(row=1, column=1)

        self.isbn_entry = StringVar()
        self.isbn_text_entry = Entry(self.window, textvariable=self.isbn_entry)
        self.isbn_text_entry.grid(row=1, column=3)

        self.listbox = Listbox(self.window, height=6, width=45)
        self.listbox.grid(row=2, column=0, columnspan=6, rowspan=6)

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.grid(row=2, column=6, rowspan=6)

        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)
        
        self.button_view_all = Button(self.window, text="View all", width=12, command=self.view_command)
        self.button_view_all.grid(row=0, column=7)

        self.button_search_entry = Button(self.window, text="Search entry", width=12, command=self.search_command)
        self.button_search_entry.grid(row=1, column=7)

        self.button_add_entry = Button(self.window, text="Add entry", width=12)
        self.button_add_entry.grid(row=2, column=7)

        self.button_update = Button(self.window, text="Update", width=12)
        self.button_update.grid(row=3, column=7)

        self.button_delete = Button(self.window, text="Delete", width=12)
        self.button_delete.grid(row=4, column=7)

        self.button_close = Button(self.window, text="Close", width=12)
        self.button_close.grid(row=5, column=7)

    def view_command(self):
        self.listbox.delete(0, 'end')
        for row in self.view():
            self.listbox.insert('end', row)

    def search_command(self):
        self.listbox.delete(0, 'end')
        for row in self.search_table(self.title_entry.get(), self.author_entry.get(), self.year_entry.get(), self.isbn_entry.get()):
            self.listbox.insert('end', row)


if __name__ == "__main__":
    window = Database_GUI('local.db')
    window.insert_values('sapiens', 'harrari', 2012, 1227)
    window.window.mainloop()
