from collections import deque
from threading import Thread, Lock
import time
from random import random

def download(item):
    print(f'downloading {item}')
    time.sleep(0.1*random())
    return f'downloaded {item}'

def resize(item):
    print(f'resizing {item}')
    time.sleep(0.1*random())
    return f'resized {item}'

def upload(item):
    print(f'uploading {item}')
    time.sleep(0.1*random())
    return f'uploaded {item}'

print(upload(resize(download('1'))))

class MyQueue:
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()

threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

for t in threads: t.start()
for i in range(10):
    download_queue.put(str(i))

while len(done_queue.items) < 10:
    pass

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print(f'processed {processed} items after polling {polled} times')
