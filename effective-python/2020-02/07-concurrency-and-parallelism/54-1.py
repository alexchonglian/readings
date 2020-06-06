class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        counter.increment(1)

from threading import Thread

how_many = 10**5
counter = Counter()

threads = [Thread(target=worker, args=(i, how_many, counter)) \
    for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

expected = how_many * 5
actual = counter.count
print('expected', expected, 'actual', actual)

from threading import Lock

class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset

counter = LockingCounter()

threads = [Thread(target=worker, args=(i, how_many, counter)) \
    for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

expected = how_many * 5
actual = counter.count
print('expected', expected, 'actual', actual)