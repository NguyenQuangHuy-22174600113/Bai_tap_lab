import tkinter as tk
from tkinter import messagebox

def positive_year_to_negative_year(positive_year):
    negative_year = -positive_year + 728
    return negative_year

def get_con_giap_image(negative_year):
    con_giap_image = open("con_giap_images/con_giap_{}.jpg".format(negative_year), "r")
    return con_giap_image

def show_result():
    input_year = int(entry_box.get())
    negative_year = positive_year_to_negative_year(input_year)
    con_giap_image = get_con_giap_image(negative_year)
    messagebox.showinfo("Result", "The negative year of {} in the Western calendar is equal to {} in the Vietnamese calendar.".format(input_year, negative_year))
    messagebox.showinfo("Con Giáp Image", con_giap_image)

root = tk.Tk()
root.title("Positive Year to Negative Year Converter")

entry_box = tk.Entry(root, width=20)
entry_box.pack()

convert_button = tk.Button(root, text="Convert", command=show_result)
convert_button.pack()

root.mainloop()
