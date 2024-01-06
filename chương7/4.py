import tkinter as tk

window = tk.Tk()
window.title("GUI Program")

label = tk.Label(window, text="Enter your name:")
label.pack()

entry_name = tk.Entry(window, width=50)
entry_name.pack()

label_id = tk.Label(window, text="Enter your ID:")
label_id.pack()

entry_id = tk.Entry(window, width=50)
entry_id.pack()

label_password = tk.Label(window, text="Enter your password:")
label_password.pack()

entry_password = tk.Entry(window, width=50)
entry_password.pack()

button = tk.Button(window, text="Submit", command=lambda: submit_info())
button.pack()

def submit_info():
    name = entry_name.get()
    id = entry_id.get()
    password = entry_password.get()
    print(f"Your information: {name}, {id}, {password}")

window.mainloop()