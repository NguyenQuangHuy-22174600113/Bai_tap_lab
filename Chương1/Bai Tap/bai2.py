class TS:
    def __init__(self, name, diemtoan, diemly, diemhoa):
        self.name = name
        self.diemtoan = diemtoan
        self.diemly = diemly
        self.diemhoa = diemhoa

    def tong_diem(self):
        return self.diemhoa + self.diemly + self.diemhoa

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"điểm toán: {self.diemtoan}")
        print(f"điểm lý: {self.diemly}")
        print(f"điểm hóa: {self.diemhoa}")

hs = []
num_hs = int(input("nhập số học sinh: "))
for i in range(num_hs):
    name = input("nhập tên học sinh: ")
    diemtoan = float(input("nhập điểm toán: "))
    diemly = float(input("nhập điểm lý: "))
    diemhoa = float(input("nhập điểm hóa: "))
    hs.append(TS(name, diemtoan, diemly, diemhoa))

trungtuyen_hs = []
for student in hs:
    if student.tong_diem() >= 20:
        trungtuyen_hs.append(student)

trungtuyen_hs.sort(key=lambda x: x.tong_diem(), reverse=True)

print("sinh viên đã trúng tuyển:")
for student in trungtuyen_hs:
    student.display_info()
    print()