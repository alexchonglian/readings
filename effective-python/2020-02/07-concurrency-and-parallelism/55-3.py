from threading import Thread
from queue import Queue
import time

my_queue = Queue(2) # try 1 2 3

def consumer():
    time.sleep(0.1)
    my_queue.get()
    print('Consumer got 1')
    my_queue.get()
    print('Consumer got 2')
    print('Consumer done')

thread = Thread(target=consumer)
thread.start()

my_queue.put(object())
print('Producer put 1')
my_queue.put(object())
print('Producer put 2')
print('Producer done')
thread.join()