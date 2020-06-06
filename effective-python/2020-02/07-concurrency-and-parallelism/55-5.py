from threading import Thread
from queue import Queue
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

class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()

class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]

for t in threads: t.start()
for i in range(10):
    download_queue.put(str(i))

download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()

print(done_queue.qsize(), 'item finished')