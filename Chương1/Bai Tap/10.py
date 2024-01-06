import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, Trung_Diem, Truc_Dai, Truc_Ngan):
        super().__init__(Trung_Diem.x, Trung_Diem.y)
        self.Truc_Dai = Truc_Dai
        self.Truc_Ngan = Truc_Ngan

    def Dien_Tich(self):
        return math.pi * self.Truc_Dai * self.Truc_Ngan

class Duong_Tron(Elip):
    def __init__(self, Trung_Diem, radius):
        super().__init__(Trung_Diem, radius * 2, radius * 2)


Trung_Diem = Diem(0, 0)
Truc_Dai = 6
Truc_Ngan = 4

elip = Elip(Trung_Diem, Truc_Dai, Truc_Ngan)
Dien_Tich = elip.Dien_Tich()

print(f"Diện tích của Elip là: {Dien_Tich}")