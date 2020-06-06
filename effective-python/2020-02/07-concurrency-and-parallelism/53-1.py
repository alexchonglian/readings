import time

def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i

numbers = [2139079, 1214759, 1516637, 1852285]

start = time.time()

for number in numbers:
    print(list(factorize(number)))

end = time.time()
delta = end - start
print(f'took {delta: .3f} seconds')

from threading import Thread

class FactorizedThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()
threads = [FactorizedThread(number) for number in numbers]
for t in threads: t.start()
for t in threads: t.join()
for t in threads: print(t.factors)
end = time.time()
delta = end - start
print(f'took {delta: .3f} seconds')