import subprocess

result = subprocess.run(
    ['echo', 'hello from child process'],
    capture_output = True,
    encoding='utf-8')

result.check_returncode()
print(dir(result))
print(result)
print(result.stdout)