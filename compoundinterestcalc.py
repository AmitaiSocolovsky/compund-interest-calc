import tkinter as tk
from tkinter import messagebox

# Function to calculate compound interest
def calculate_interest():
    try:
        # Get user input from the Entry widgets
        principle = float(principle_entry.get())
        rate = float(rate_entry.get())
        time = int(time_entry.get())

        # make sure inputs are valid 
        if principle <= 0:
            messagebox.showerror("Input Error", "Principle can't be less than or equal to zero.")
            return
        if rate <= 0:
            messagebox.showerror("Input Error", "Rate can't be less than or equal to zero.")
            return
        if time <= 0:
            messagebox.showerror("Input Error", "Time can't be less than or equal to zero.")
            return

        # Apply rounding
        principle = round(principle)
        rate = round(rate, 2)

        # Compound Interest Formula
        total = principle * pow((1 + rate / 100), time)

        # Display result 
        result_label.config(text=f"Balance after {time} year(s): ${total:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main app window
root = tk.Tk()
root.title("Compound Interest Calculator")
root.geometry("350x300")

# UI Elements (Labels & Entry Fields)
tk.Label(root, text="Enter Principal Amount:").pack(pady=5)
principle_entry = tk.Entry(root)
principle_entry.pack()

tk.Label(root, text="Enter Rate (%):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Enter Time (Years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack()

# Calculate Button
calculate_btn = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
