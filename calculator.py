import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Arithmetic Calculator")
window.configure(bg="white")

entry = tk.Entry(window, width=30, justify=tk.RIGHT, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.configure(bg="lightyellow", fg="black", bd=5)

button_padding = 5

button_colors = {"1": "lightgray", "2": "lightgray", "3": "lightgray", "4": "lightgray",
                 "5": "lightgray", "6": "lightgray", "7": "lightgray", "8": "lightgray", "9": "lightgray"}

for i in range(1, 10):
    button = tk.Button(window, text=str(i), width=4, height=2, font=("Arial", 16), bg=button_colors[str(i)], command=lambda num=i: entry.insert(tk.END, str(num)))
    button.grid(row=1 + (i-1)//3, column=(i-1)%3, padx=button_padding, pady=button_padding, ipadx=10, ipady=10)  # Set ipadx and ipady to make the buttons cubic

zero_button = tk.Button(window, text="0", width=4, height=2, font=("Arial", 16), bg="lightgray", command=lambda: entry.insert(tk.END, "0"))
zero_button.grid(row=4, column=1, padx=button_padding, pady=button_padding, ipadx=10, ipady=10)  # Set ipadx and ipady to make the buttons cubic

operator_colors = {"+": "gray", "-": "gray", "*": "gray", "/": "gray"}

operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, width=4, height=2, font=("Arial", 16), bg=operator_colors[operator], command=lambda op=operator: entry.insert(tk.END, op))
    button.grid(row=1 + i, column=3, padx=button_padding, pady=button_padding, ipadx=10, ipady=10)  # Set ipadx and ipady to make the buttons cubic

equals_button = tk.Button(window, text="=", width=4, height=2, font=("Arial", 16), bg="gray", fg="white", command=calculate)
equals_button.grid(row=4, column=2, padx=button_padding, pady=button_padding, ipadx=10, ipady=10)  # Set ipadx and ipady to make the button cubic

clear_button = tk.Button(window, text="C", width=4, height=2, font=("Arial", 16), bg="gray", fg="white", command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=4, column=0, padx=button_padding, pady=button_padding, ipadx=10, ipady=10)  # Set ipadx and ipady to make the button cubic

window.mainloop()
