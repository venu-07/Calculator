import tkinter as tk
from math import *

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/",
    "sin", "cos", "tan", "^2",
    "sqrt", "(", ")", "pi",
]

row, col = 0, 0
buttons = []

for btn_text in button_texts:
    button = tk.Button(button_frame, text=btn_text, font=("Helvetica", 15), padx=20, pady=20)
    button.grid(row=row, column=col, padx=8, pady=8)
    button.bind("<Button-1>", on_button_click)
    buttons.append(button)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()