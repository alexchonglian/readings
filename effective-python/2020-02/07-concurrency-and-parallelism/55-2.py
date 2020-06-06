from threading import Thread
from queue import Queue

my_queue = Queue()

def consumer():
    print('consumer waiting')
    my_queue.get()
    print('consumer done')

thread = Thread(target=consumer)
thread.start()

print('Producer putting')
my_queue.put(object())
print('Producer done')
thread.join()