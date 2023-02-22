import tkinter as tk
from tkinter import ttk
import summary_scrap as ss


def submit():
    stock_name = input_stock.get()
    print(stock_name)
    stat_header = tk.Label(text=f'Summary of the Statistics of {stock_name}')
    stat_header.pack()


# create the main window
root = tk.Tk()
root.title('Stock Viewer')
root.geometry('600x300')
label = tk.Label(text='Enter a Value')
input_stock = tk.Entry()
tree = ttk.Treeview(root, columns=("Header", "Value"), show='headings')
enter = tk.Button(root, text='Submit', command=submit)

# Column Headings
tree.heading("Header", text="Header")
tree.heading("Value", text="Value")

# Inserting Data
ins = ss.get_summary()
for k in ins:
    tree.insert('', tk.END, values=k)

# Packing Widgets
# label.pack()
# input_stock.pack(pady=10)
# enter.pack()
# tree.pack()

# Start
root.mainloop()
