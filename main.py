import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("350x500")
root.resizable(False, False)
root.configure(background="#7f8291")


def click_button(button):
    value_text = entry.get()
    if button == 'AC':
        entry.delete(0, tk.END)
    elif button == '+/-':
        try:
            result = float(value_text) * -1
            if result.is_integer():
                result = int(result)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif button == '%':
        try:
            result = float(value_text) / 100
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif button == ',':
        entry.insert(tk.END, '.')
    elif button == '=':
        try:
            result = eval(value_text)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, button)

buttons = [
    'AC', '+/-', '%', '/', '7',
    '8', '9', '*', '4', '5',
    '6', '-', '1', '2', '3',
    '+', '0', ',', '='
]

entry = tk.Entry(root, font=('Arial', 55), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='ew')
entry.configure(background="#e5e6e9")

row = 1
column = 0

for i in range(4):
    root.grid_columnconfigure(i, weight=1, uniform="equal")
    for i in range(5):
        root.grid_rowconfigure(i + 1, weight=1, uniform="equal")

for button in buttons:
    if button == '0':
        btn1 = tk.Button(root, text=button, font=('Arial', 24), background='#eeff8e',
                         command=lambda b=button: click_button(b))
        btn1.grid(row=row, column=column, columnspan=2, sticky="nsew", padx=5, pady=5)
        column += 2
    else:
        btn1 = tk.Button(root, text=button, font=('Arial', 18), background='#eeff8e',
                         command=lambda b=button: click_button(b))
        btn1.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        column += 1

    if column > 3:
        column = 0
        row += 1

root.mainloop()
