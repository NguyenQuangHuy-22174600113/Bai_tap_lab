import tkinter as tk

# Define the main window
window = tk.Tk()
window.title("Menu-Based Application")

# Create a menu
menu = tk.Menu(window)
window.config(menu=menu)

# Add items to the menu
menu.add_command(label="Chương1", command=lambda: print("Chương1 selected"))
menu.add_command(label="Chương2", command=lambda: print("Chương2 selected"))
menu.add_command(label="chương3", command=lambda: print("Chương3 selected"))

# Create a button to display the menu
button = tk.Button(window, text="Display Menu", command=lambda: menu.move(window.which))
button.pack()

# Run the application
window.mainloop()
