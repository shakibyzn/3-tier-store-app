# graphical user interface
import tkinter 
from tkinter import ttk
import businesslogic as bs
import time
from ttkthemes import themed_tk as tk
from tkinter import messagebox as mb

# inserting into the database
def f():
    try:
        pr = bs.Product(e1.get(), e2.get(), e3.get())
        output_error = pr.insert()
    except IndexError:
        mb.showerror("BAM", "You didn't buy anything!")

# showing what each customer bought
def g(): 
    list_of_items = bs.Product.show()
    Lb = tkinter.Listbox(master, width = 30)
    for i, item in enumerate(list_of_items):  
        Lb.insert(i, (item[0], item[1], item[2], item[3]))  
        Lb.grid(row=3, column=3)

# showing the history of products that a customer bought
def purchase_history():
    try:
        full_name = e4.get()
        purchase_hist = bs.Product.show_history(full_name.split(" "))
        Lb = tkinter.Listbox(master, width = 20)
        for i, item in enumerate(purchase_hist):  
            Lb.insert(i, (item[0], item[1]))  
            Lb.grid(row=3, column=18)
    except IndexError:
        mb.showerror("BAM", "Sorry, nothing to show!")

# setting the Adapta theme
master = tk.ThemedTk() 
master.get_themes()
master.set_theme('adapta')

# Labels
ttk.Label(master, text='CustomerFirstName').grid(row=0, column=2) 
ttk.Label(master, text='CustomerFamilyName').grid(row=1, column=2) 
ttk.Label(master, text='ProductName').grid(row=2, column=2) 
ttk.Label(master, text='Enter Customer FullName').grid(row=0, column=17) 

# Inputs
e1 = ttk.Entry(master) 
e2 = ttk.Entry(master) 
e3 = ttk.Entry(master)
e4 = ttk.Entry(master)

e1.grid(row=0, column=3, padx=2) 
e2.grid(row=1, column=3, padx=2) 
e3.grid(row=2, column=3, padx=2)
e4.grid(row=0, column=18, padx=2)

# Buttons
button = ttk.Button(master, text='BUY', width=5, command=f)
button.grid(row=1, column=17)
button = ttk.Button(master, text='SHOW', width=6, command=g)
button.grid(row=2, column=17)
button = ttk.Button(master, text='PURCHASE HISTORY', width=18, command=purchase_history)
button.grid(row=1, column=18, padx=5)

tkinter.mainloop() 
