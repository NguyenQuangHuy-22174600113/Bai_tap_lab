import threading

def In_Chan(start, end):
    for num in range(start, end + 1, 2):
        print(f"Số chẵn: {num}")

def In_Le(start, end):
    for num in range(start + 1, end + 1, 2):
        print(f"Số lẻ: {num}")

Nguong_Dung = 20

Luong_Chan = threading.Thread(target=In_Chan, args=(0, Nguong_Dung))
Luong_Le = threading.Thread(target=In_Le, args=(0, Nguong_Dung))

Luong_Chan.start()
Luong_Le.start()

Luong_Chan.join()
Luong_Le.join()

print("Hoàn thành")