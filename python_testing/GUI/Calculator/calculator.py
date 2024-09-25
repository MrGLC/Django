import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def plot_example():
    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()

def on_click(event=None):
    # Get the value from entry, evaluate it, and update the entry with the result
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

app = tk.Tk()
app.title("Calculator")

entry = tk.Entry(app, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('5', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('5', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('5', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('5', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(app, text=text, height=2, width=9, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col)
    if text == '=':
        button.bind('<Button-1>', on_click)
        app.bind('<Return>', on_click)

# Add a Plot button to the calculator
plot_button = tk.Button(app, text='Plot', height=2, width=9, command=plot_example)
plot_button.grid(row=5, column=0, columnspan=4)

app.mainloop()
