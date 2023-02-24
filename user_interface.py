import tkinter as tk
from tkinter import ttk, font
import summary_scrap as ss


class UserI:

    def __init__(self, master):
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Helvetica", size=10)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Stock Viewer')
        self.master.geometry('400x350')
        self.en_val = tk.Label(self.master, text='Enter a Stock Ticker:')
        self.inp_stock = tk.Entry(self.master)
        self.tree = ttk.Treeview(self.master, columns=("Header", "Value"), show='headings')
        self.tree = ttk.Treeview(self.master, columns=("Header", "Value"), show='headings')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Helvetica', 10))
        self.bt_submit = tk.Button(self.master, text='Submit', command=lambda: UserI.submit(self))
        self.tree.heading("Header", text="Statistic")
        self.tree.heading("Value", text="Value")
        self.stat_header = None
        self.cur_price = None
        UserI.pack_display(self, 'first')

    def submit(self):
        self.tree.delete(*self.tree.get_children())
        stock_name = self.inp_stock.get().upper()
        self.en_val.grid_forget()
        self.inp_stock.grid_forget()
        self.bt_submit.grid_forget()
        if self.stat_header is not None:
            self.stat_header.grid_forget()
            self.cur_price.grid_forget()
        if not ss.existing_stock(stock_name):
            self.stat_header = tk.Label(text=f'{stock_name} is not a valid ticker', font=('Helvetica', 12, 'bold'))
            self.en_val = tk.Label(self.master, text='Enter a Stock Ticker:')
            self.stat_header.grid(row=1, column=0, pady=2, padx=2, columnspan=5)
            UserI.pack_display(self, 'first')
            return
        self.stat_header = tk.Label(text=f'Summary of the Statistics of {stock_name}', font=('Helvetica', 12, 'bold'))
        UserI.insert_data(self, stock_name)
        self.stat_header.grid(row=0, column=0, pady=2, padx=2, columnspan=5)
        self.cur_price = tk.Label(text=ss.get_cur_price(stock_name)[0], fg=ss.get_cur_price(stock_name)[1])
        self.cur_price.grid(row=1, column=0, pady=2, columnspan=5)
        self.en_val = tk.Label(self.master, text='Enter Another Stock Ticker:')
        UserI.pack_display(self, 'post')

    def pack_display(self, loc):
        if loc == 'first':
            self.en_val.grid(row=0, column=0, pady=2)
            self.inp_stock.grid(row=0, column=1, pady=2)
            self.bt_submit.grid(row=0, column=2, pady=2, padx=2)
            self.tree.grid(row=4, column=0, rowspan=5, columnspan=5)
        else:
            self.en_val.grid(row=8, column=0, pady=2)
            self.inp_stock.grid(row=8, column=1, pady=2)
            self.bt_submit.grid(row=8, column=2, pady=2, padx=2)
            self.tree.grid(row=2, column=0, rowspan=5, columnspan=5)

    def insert_data(self, ticker):

        ins = ss.get_summary(ticker)
        for k in ins:
            self.tree.insert('', tk.END, values=k)


root = tk.Tk()
app = UserI(root)
root.mainloop()
