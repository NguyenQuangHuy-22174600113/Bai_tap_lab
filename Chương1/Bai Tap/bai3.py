class PS:
    def __init__(self, tuso=0, mauso=2):
        self.tuso = tuso
        self.mauso = mauso

    def Hop_le(self):
        return self.mauso != 0
    
    def input_PhanSo(self):
        self.tuso = int(input("nhập tử số: "))
        self.mauso = int(input("nhập mẫu số: "))
    
        if not self.Hop_le():
            print("mẫu số không được bằng 0.")
            self.input_PhanSo()
    
    def display(self):
        print(f"{self.tuso}/{self.mauso}")

PhanSo = PS()
PhanSo.input_PhanSo()
PhanSo.display()