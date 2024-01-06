import threading

lock = threading.Lock()

def print_even_numbers(limit):
    for i in range(2, limit+1, 2):
        print(i, end=" ")
        lock.acquire()
        print(i, end=" ")
        lock.release()

def print_odd_numbers(limit):
    for i in range(1, limit+1, 2):
        lock.acquire()
        print(i, end=" ")
        lock.release()

limit = 10

even_thread = threading.Thread(target=print_even_numbers, args=(limit,))
odd_thread = threading.Thread(target=print_odd_numbers, args=(limit,))

even_thread.start()

odd_thread.start()

even_thread.join()
odd_thread.join()