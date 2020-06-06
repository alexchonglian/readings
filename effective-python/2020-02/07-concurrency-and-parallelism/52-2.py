import subprocess

proc = subprocess.Popen(['sleep', '0.00001'])
while proc.poll() is None:
    print('working')
print('exit status', proc.poll())
