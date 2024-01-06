import threading
import random
import time

def thread_function():
    print("Chương trình đang chạy...")
    value = random.randint(0, 100)
    print("Giá trị ngẫu nhiên từ 0 đến 100: ", value)

thread = threading.Thread(target=thread_function)
thread.start()

thread.join()