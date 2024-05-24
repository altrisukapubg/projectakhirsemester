import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Calculator App")

# Create style object
style = Style(theme="minty")

# Create a frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

# Create entry widgets
entry_num1 = ttk.Entry(frame)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = ttk.Entry(frame)
entry_num2.grid(row=1, column=0, padx=5, pady=5)

# Create label for result
label_result = ttk.Label(frame, text="Result: ")
label_result.grid(row=2, column=0, padx=5, pady=5)

# Create button to calculate
btn_calculate = ttk.Button(frame, text="Calculate", command=calculate)
btn_calculate.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()