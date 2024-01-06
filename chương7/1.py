import tkinter as tk

window = tk.Tk()
window.title("GUI Program")

label = tk.Label(window, text="Enter your name:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

button = tk.Button(window, text="Submit", command=lambda: print(f"Your name is {entry.get()}"))
button.pack()

window.mainloop()