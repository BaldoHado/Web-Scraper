import tkinter as tk
from tkinter import ttk
import summary_scrap as ss


def submit():
    stock_name = inp_stock.get()
    print(stock_name)
    stat_header = tk.Label(text=f'Summary of the Statistics of {stock_name}')
    stat_header.grid(row=1, column=0, pady=2, padx=2, columnspan=2)


# create the main window
root = tk.Tk()
root.title('Stock Viewer')
root.geometry('600x300')
en_val = tk.Label(text='Enter a Value')
inp_stock = tk.Entry()
tree = ttk.Treeview(root, columns=("Header", "Value"), show='headings')
bt_submit = tk.Button(root, text='Submit', command=submit)

# Column Headings
tree.heading("Header", text="Header")
tree.heading("Value", text="Value")

# Inserting Data
ins = ss.get_summary()
for k in ins:
    tree.insert('', tk.END, values=k)

# Packing Widgets
en_val.grid(row=0, column=0, pady=2)
inp_stock.grid(row=0, column=1, pady=2)
bt_submit.grid(row=0, column=2, pady=2, padx=2)
tree.grid(row=2, column=0, rowspan=5, columnspan=5)
# label.pack()
# input_stock.pack(pady=10)
# enter.pack()
# tree.pack()

# Start
root.mainloop()
