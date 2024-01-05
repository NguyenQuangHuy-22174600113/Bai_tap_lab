class Date:
    def __init__(self, day=26, month=9, year=2023):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day}/{self.month}/{self.year}"


class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name
        self.birth_date = birth_date
        self.join_date = join_date

    def display(self):
        print(f"Name: {self.name}")
        print(f"Birth date: {self.birth_date.display()}")
        print(f"Join date: {self.join_date.display()}")

birth_date = Date(7, 1, 2004)
join_date = Date(26, 9, 2023)
employee = Employee("Nguyễn Quang Huy", birth_date, join_date)
employee.display()
