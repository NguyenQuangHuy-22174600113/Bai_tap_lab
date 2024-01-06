import tkinter as tk

class TaxiGUI(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.button = tk.Button(self, text="Tính cước taxi", command=self.calculate_fare)
        self.button.pack(padx=10, pady=10)
        self.entry = tk.Entry(self, textvariable=self.fare)
        self.entry.pack(padx=10, pady=10)

    def calculate_fare(self):
        total_fare = self.fare.get()
        fare = total_fare * 0.15
        taxi = fare / 10
        num_people = total_fare / taxi
        self.show_result(fare, taxi, num_people)

    def show_result(self, fare, taxi, num_people):
        result = f"Cước taxi: {fare}\nSố lượng người: {num_people}"
        self.result.set(result)

if __name__ == "__main__":
    app = TaxiGUI()
app.mainloop()