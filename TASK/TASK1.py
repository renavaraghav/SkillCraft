import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        value = float(entry_value.get())
        scale = scale_var.get()

        if scale == 'C':
            f = (value * 9/5) + 32
            k = value + 273.15
            result.set(f"{value}°C = {f:.2f}°F, {k:.2f}K")
        elif scale == 'F':
            c = (value - 32) * 5/9
            k = c + 273.15
            result.set(f"{value}°F = {c:.2f}°C, {k:.2f}K")
        elif scale == 'K':
            c = value - 273.15
            f = (c * 9/5) + 32
            result.set(f"{value}K = {c:.2f}°C, {f:.2f}°F")
        else:
            messagebox.showerror("Invalid Input", "Please select a valid scale.")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid numeric value.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.configure(bg="#f0f4f7")

tk.Label(root, text="🌡 Temperature Converter", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

frame_input = tk.Frame(root, bg="#f0f4f7")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Enter Value:", font=("Arial", 12), bg="#f0f4f7").grid(row=0, column=0, padx=5)
entry_value = tk.Entry(frame_input, font=("Arial", 12), width=10)
entry_value.grid(row=0, column=1, padx=5)

scale_var = tk.StringVar(value="C")
tk.Label(frame_input, text="Scale:", font=("Arial", 12), bg="#f0f4f7").grid(row=0, column=2, padx=5)

scale_menu = tk.OptionMenu(frame_input, scale_var, "C", "F", "K")
scale_menu.config(font=("Arial", 12))
scale_menu.grid(row=0, column=3, padx=5)

convert_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=15, command=convert_temperature)
convert_btn.pack(pady=15)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12, "italic"), bg="#f0f4f7", fg="#007acc").pack(pady=10)

root.mainloop()