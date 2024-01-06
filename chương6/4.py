import threading

def Giai_Thua(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def Luong_Giai_Thua(numbers):
    List_Luong = []
    List_Ket_Qua = {}

    def Luu_Ket_Qua(number):
        List_Ket_Qua[number] = Giai_Thua(number)

    for i in numbers:
        Luong = threading.Thread(target=Luu_Ket_Qua, args=(i,))
        Luong.start()
        List_Luong.append(Luong)

    for Luong in List_Luong:
        Luong.join()

    return List_Ket_Qua

List_Can_Tinh = [1, 4, 5, 6, 7, 8, 9, 11]

Tinh_Toan = Luong_Giai_Thua(List_Can_Tinh)

for i, j in Tinh_Toan.items():
    print(f"Giai thừa của {i} là {j}")