import threading
import time

def worker():
    print("Thread starting")
    time.sleep(1)
    raise RuntimeError("Something went wrong!")  # Thread crashes here
    print("This won't print")

def safe_worker():
    print("Safe thread running")
    time.sleep(2)
    print("Safe thread done")

# Start threads
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=safe_worker)

t1.start()
t2.start()

t1.join()
t2.join()
print("Main program continues")
