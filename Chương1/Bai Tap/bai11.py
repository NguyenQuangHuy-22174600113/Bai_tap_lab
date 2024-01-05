import math

class TamGiac:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def ChuVi(self):
        return self.side1 + self.side2 + self.side3

    def DienTich(self):
        s = self.ChuVi() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


class TamGiacVuong(TamGiac):
    def __init__(self, side1, side2):
        super().__init__(side1, side2, math.sqrt(side1**2 + side2**2))

    def DienTich(self):
        return self.side1 * self.side2 / 2

class TamGiacCan(TamGiac):
    def __init__(self, base, side):
        super().__init__(base, side, side)


class TamGiacDeu(TamGiacCan):
    def __init__(self, side):
        super().__init__(side, side)

    def DIenTich(self):
        return (math.sqrt(3) / 4) * self.side1**2
