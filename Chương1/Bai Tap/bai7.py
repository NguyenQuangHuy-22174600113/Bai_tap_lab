class Date:
    def __init__(self, day=26, month=9, year=2023):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def next(self):
        self.day += 1
        if self.day > 30:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

d = Date(31, 12, 2029)
d.display()
d.next()
d.display()