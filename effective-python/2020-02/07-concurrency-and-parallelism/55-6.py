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
    def __init__(self, id, func, in_queue, out_queue):
        super().__init__()
        self.id = id
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

def start_threads(count, *args):
    threads = [StoppableWorker(i, *args) for i in range(count)]
    for t in threads: t.start()
    return threads

def stop_threads(closable_queue, threads):
    for _ in threads:
        closable_queue.close()
    closable_queue.join()
    for t in threads: t.join()

download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

download_threads = start_threads(3, download, download_queue, resize_queue)
resize_threads   = start_threads(4, resize, resize_queue, upload_queue)
upload_threads   = start_threads(5, upload, upload_queue, done_queue)

for i in range(10):
    download_queue.put(str(i))

stop_threads(download_queue, download_threads)
stop_threads(resize_queue, resize_threads)
stop_threads(upload_queue, upload_threads)

print(done_queue.qsize(), 'item finished')

