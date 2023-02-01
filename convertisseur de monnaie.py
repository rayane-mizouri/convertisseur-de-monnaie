from tkinter import *
from tkinter import ttk

gui = Tk()
gui.geometry("300x350")

def convert():
    eur = "eur"
    usd = "usd"
    rub = "rub"
    lists=[eur, usd, rub]

    final_amount_entry.delete(0, END)
    if initial_currency_entry.get() == eur and final_currency_entry.get() == usd:
        conversion = float(int(amount_entry.get()) * 1.2)
        conversion = round(conversion, 5)
        final_amount_entry.insert(0, conversion)

    elif initial_currency_entry.get() == usd and final_currency_entry.get() == eur:
        conversion = float(int(amount_entry.get()) / 1.2)
        conversion = round(conversion, 5)
        final_amount_entry.insert(0,conversion)

    elif initial_currency_entry.get() == eur and final_currency_entry.get() == rub:
        conversion = float(int(amount_entry.get()) * 75)
        conversion = round(conversion, 5)
        final_amount_entry.insert(0,conversion)

    elif initial_currency_entry.get() == usd and final_currency_entry.get() == rub:
        conversion = float(int(amount_entry.get()) * 74.8)
        conversion = round(conversion, 5)
        final_amount_entry.insert(0,conversion)

    elif initial_currency_entry.get() == rub and final_currency_entry.get() == eur:
        conversion = float(int(amount_entry.get()) / 75)
        conversion = round(conversion, 5)
        final_amount_entry.insert(0,conversion)

    elif initial_currency_entry.get() == rub and final_currency_entry.get() == usd:
        conversion = float(int(amount_entry.get()) / 74.8)
        conversion = round(conversion, 4)
        final_amount_entry.insert(0,conversion)

    elif initial_currency_entry.get() == final_currency_entry.get():
        final_amount_entry.insert(0,amount_entry.get())

    elif initial_currency_entry.get() or final_currency_entry.get() != lists:
        final_amount_entry.insert(0, "error")

    history_entry.config(text=history_entry.cget("text") + "\n" + amount_entry.get() + " " + initial_currency_entry.get() + " --> " + final_amount_entry.get() + " " + final_currency_entry.get())


notebook = ttk.Notebook(gui)
notebook.pack(pady=5)

convert_frame = Frame(notebook, width=300, height=320)
history_frame = Frame(notebook, width=300, height=320)

notebook.add(convert_frame,text="Convertisseur")
notebook.add(history_frame,text="Historique")

amount = Label(convert_frame, text="Montant à convertir")
amount.pack(pady=10)
amount_entry = Entry(convert_frame)
amount_entry.pack()

initial_currency = Label(convert_frame, text="Devise initial")
initial_currency.pack(pady=10)
list = ["eur", "usd","rub"]
initial_currency_entry = ttk.Combobox(convert_frame, values=list)
initial_currency_entry.pack()



final_currency = Label (convert_frame, text="Devise final")
final_currency.pack(pady=10)
final_currency_entry = ttk.Combobox(convert_frame, values=list)
final_currency_entry.pack()


final_amount = Label (convert_frame, text="Montant final")
final_amount.pack(pady=10)
final_amount_entry = Entry(convert_frame)
final_amount_entry.pack()

button_frame = Button(convert_frame,text="convertir",command=convert)
button_frame.pack(pady=20)
history = Label (history_frame, text="Votre histrique de conversion")
history.pack(pady=10)
history_entry = Label(history_frame)
history_entry.place(y=40)




gui.mainloop()