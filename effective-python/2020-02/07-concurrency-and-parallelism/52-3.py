import subprocess
import time

start = time.time()
sleep_procs = [subprocess.Popen(['sleep', '1']) for _ in range(10)]
for proc in sleep_procs:
    proc.communicate()

end = time.time()
delta = end - start
print(f'finished in {delta:.3} seconds')