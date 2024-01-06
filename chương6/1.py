import threading

def In_Ten():
    print("Tên luồng:", threading.current_thread().name)

List_Luong = []
So_Luong = 5  

for i in range(So_Luong):
    thread = threading.Thread(target=In_Ten)
    List_Luong.append(thread)
    thread.start()

for thread in List_Luong:
    thread.join()