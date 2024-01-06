import threading

def So_Chan(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print("Số chẵn:", num)


def So_Le(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(f"Số lẻ:", num)

So_Dau = 30
So_Cuoi = 50

Luong_Chan = threading.Thread(target=So_Chan, args=(So_Dau, So_Cuoi))
Luong_Le = threading.Thread(target=So_Le, args=(So_Dau, So_Cuoi))

Luong_Chan.start()
Luong_Le.start()

Luong_Chan.join()
Luong_Le.join()

print("Tất cả các số đã được in")