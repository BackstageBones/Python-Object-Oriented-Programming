from tkinter import Tk, Label, Entry, StringVar, Listbox, Scrollbar
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

        self.title_text_entry = Entry(self.window, textvariable=StringVar())
        self.title_text_entry.grid(row=0, column=1)

        self.author_text_entry = Entry(self.window, textvariable=StringVar())
        self.author_text_entry.grid(row=0, column=3)

        self.year_text_entry = Entry(self.window, textvariable=StringVar())
        self.year_text_entry.grid(row=1, column=1)

        self.isbn_text_entry = Entry(self.window, textvariable=StringVar())
        self.isbn_text_entry.grid(row=1, column=3)

        self.listbox = Listbox(self.window, height=6, width=45)
        self.listbox.grid(row=2, column=0, columnspan=8, rowspan=6)

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.grid(row=3, column=6, rowspan=6)

        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)


if __name__ == "__main__":
    window = Database_GUI('local')
    window.window.mainloop()
