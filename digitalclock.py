import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Create a tkinter window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(window, font=("Arial", 80), bg="black", fg="white")
clock_label.pack(fill=tk.BOTH, expand=1)

# Update the time initially and start the clock
update_time()

# Start the tkinter event loop
window.mainloop()
