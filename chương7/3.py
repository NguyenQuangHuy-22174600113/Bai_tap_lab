import tkinter as tk

window = tk.Tk()
window.title("GUI Program")

label = tk.Label(window, text="Enter your name:", font=("Arial", 12, "bold"))
label.pack()

button = tk.Button(window, text="Submit", command=lambda: print("Your name is", label.get()))
button.pack()

label.config(font=("Courier", 10, "italic"))

window.mainloop()