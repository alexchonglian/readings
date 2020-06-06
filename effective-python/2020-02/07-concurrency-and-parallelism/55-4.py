from threading import Thread
from queue import Queue
import time

in_queue = Queue()

def consumer():
    print('Consumer waiting')
    work = in_queue.get()
    print('Consumer working')
    time.sleep(0.5)
    print('Consumer done')
    in_queue.task_done()

thread = Thread(target=consumer)
thread.start()

print('Producer putting')
in_queue.put(object())
print('Producer waiting')
in_queue.join()
print('Producer done')
thread.join()