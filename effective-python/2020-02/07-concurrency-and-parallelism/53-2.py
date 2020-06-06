import select
import socket
from threading import Thread
import time

def slow():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow()
end = time.time()
delta = end - start
print(f'took {delta: .3f} seconds')

def compute_helicopter_location(i):
    print(f'compute_helicopter_location {i}')
start = time.time()
threads = [Thread(target=slow) for _ in range(5)]
for t in threads: t.start()
for i in range(5): compute_helicopter_location(i)
for t in threads: t.join()
end = time.time()
delta = end - start
print(f'took {delta: .3f} seconds')