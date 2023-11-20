import tkinter as tk
from tkinter import *
import pandas as pd
import updateSheets as us

root = Tk()
root.config(width=900, height=100)

# Label Confirmacion
confirmLabel = Label(root, text="")

# Nombre
nameLabel = Label(root, text="Name")
nameLabel.place(x=50, y=10)

entryN = tk.Entry()
entryN.place(x=10, y=30)

# Apellido
LastNameLabel = Label(root, text="LastName")
LastNameLabel.place(x=180, y=10)

entryL = tk.Entry()
entryL.place(x=150, y=30)

# Telephone
telephoneLabel = Label(root, text="Telephone")
telephoneLabel.place(x=320, y=10)

entryT = tk.Entry()
entryT.place(x=290, y=30)

# Address
addressLabel = Label(root, text="Address")
addressLabel.place(x=465, y=10)

entryA = tk.Entry()
entryA.place(x=430, y=30)

# Answer & Notes
answer = Label(root, text="Answer & Notes")
answer.place(x=590, y=10)

entryR = tk.Entry()
entryR.place(x=570, y=30)

# Pandas
client_data = pd.read_csv("data/ClientDataTrabajo.csv")


def get_entry_value():
    value = (f'{entryN.get()} | {entryL.get()} | {entryT.get()} '
             f'| {entryA.get()} | {entryR.get()}')

    data = {
        'Name': [entryN.get()],
        'LastName': [entryL.get()],
        'Telephone': [entryT.get()],
        'Address': [entryA.get()],
        'Answer': [entryR.get()]
    }
    print(value)

    confirmLabel.config(text=value)
    confirmLabel.place(x=50, y=65)

    df = pd.DataFrame(data)
    df.to_csv('data/ClientDataTrabajo.csv', mode='a', index=False, header=False)
    us.update_values(entryN.get(), entryL.get(), entryT.get(), entryA.get(), entryR.get())

    entryN.delete(0,END)
    entryL.delete(0, END)
    entryT.delete(0, END)
    entryA.delete(0, END)
    entryR.delete(0, END)


# Button write on Excel
addbutton = tk.Button(root, text="Send", width=25, command=get_entry_value)
addbutton.place(x=700, y=25)


root.mainloop()
