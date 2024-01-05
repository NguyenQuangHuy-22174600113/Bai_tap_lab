class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def tinh_chu_vi(self):
        return(self.length + self.width) * 2

    def tinh_dien_tich(self):
        return(self.length * self.width)

    def in_thong_tin(self):
        print(f"độ dài 2 cạnh: {self.length}, {self.width}")
        print(f"chu vi là:{self.tinh_chu_vi()}")
        print(f"diện tích là:{self.tinh_dien_tich()}")

# tạo đối tượng HinhChuNhat
rtl = rectangle(3, 12)
rtl.in_thong_tin()