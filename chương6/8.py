import threading

my_list = []

def read_list():
    for item in my_list:
        print(item)

def write_list(item):
    my_list.append(item)
    print(f"Wrote {item} to the list")

first_thread = threading.Thread(target=read_list)
second_thread = threading.Thread(target=write_list)

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()