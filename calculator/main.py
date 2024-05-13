import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def create_button(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Segoe UI", 18), bd=3, relief=tk.RAISED)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_click)
    return button

root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x550")
root.configure(bg="#f0f0f0")

# Heading label
heading_label = tk.Label(root, text="Calculator", font=("Segoe UI", 24, "bold"), bg="#f0f0f0")
heading_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

# Entry widget
entry = tk.Entry(root, font=("Segoe UI", 28), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="ew")

# Buttons
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("C", 6, 0, 4)
]

for button in buttons:
    create_button(*button)

# Configure grid weights to make buttons expandable
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
