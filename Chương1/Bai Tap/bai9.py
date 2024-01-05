import math

class DaGiac:
    def __init__(self, n_sides, side_length):
        self.n_sides = n_sides
        self.side_length = side_length
    
    def ChuVi(self):
        return self.n_sides * self.side_length

class HinhBinhHanh(DaGiac):
    def __init__(self, side_a, side_b, angle_in_degrees):
        super().__init__(2, side_a + side_b)
        self.side_a = side_a
        self.side_b = side_b
        self.angle = math.radians(angle_in_degrees)

    def DienTich(self):
        return self.side_a * self.side_b * math.sin(self.angle)

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b, 90)

class Hinhvuong(HinhChuNhat):
    def __init__(self, side):
        super().__init__(side, side)

DaGiac = DaGiac(2, 4)
print(f"DaGiac ChuVi: {DaGiac.ChuVi()}")

HinhBinhHanh = HinhBinhHanh(10, 20, 30)
print(f"HinhBinhHanh ChuVi: {HinhBinhHanh.ChuVi()}")
print(f"HinhBinhHanh DienTich: {HinhBinhHanh.DienTich()}")

HinhChuNhat = HinhChuNhat(5, 10)
print(f"HinhChuNhat ChuVi: {HinhChuNhat.ChuVi()}")
print(f"HinhChuNhat DienTich: {HinhChuNhat.DienTich()}")

Hinhvuong = Hinhvuong(5)
print(f"Hinhvuong ChuVi: {Hinhvuong.ChuVi()}")
print(f"Hinhvuong DienTich: {Hinhvuong.DienTich()}")
