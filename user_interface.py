import tkinter as tk
from tkinter import ttk
import summary_scrap as ss


class UserI:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Stock Viewer')
        self.master.geometry('600x300')
        self.en_val = tk.Label(text='Enter a Value')
        self.inp_stock = tk.Entry()
        self.tree = ttk.Treeview(self.master, columns=("Header", "Value"), show='headings')
        self.bt_submit = tk.Button(self.master, text='Submit', command=lambda: UserI.submit(self))
        self.tree.heading("Header", text="Header")
        self.tree.heading("Value", text="Value")
        UserI.pack_display(self)

    def submit(self):
        self.tree.delete(*self.tree.get_children())
        stock_name = self.inp_stock.get()
        stat_header = tk.Label(text=f'Summary of the Statistics of {stock_name}')
        UserI.insert_data(self, stock_name)
        stat_header.grid(row=1, column=0, pady=2, padx=2, columnspan=2)
        UserI.pack_display(self)

    def pack_display(self):
        self.en_val.grid(row=0, column=0, pady=2)
        self.inp_stock.grid(row=0, column=1, pady=2)
        self.bt_submit.grid(row=0, column=2, pady=2, padx=2)
        self.tree.grid(row=2, column=0, rowspan=5, columnspan=5)

    def insert_data(self, ticker):

        ins = ss.get_summary(ticker)
        for k in ins:
            self.tree.insert('', tk.END, values=k)


root = tk.Tk()
app = UserI(root)
root.mainloop()