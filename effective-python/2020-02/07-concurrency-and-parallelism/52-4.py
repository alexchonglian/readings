import subprocess
import os

def run_encrypt(data):
    env = os.environ.copy()
    #print(env)
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env = env,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE
    )

    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

def run_hash(input_stdin):
    return subprocess.Popen(
        ['openssl', 'dgst', '-whirlpool', '-binary'],
        stdin = input_stdin,
        stdout = subprocess.PIPE
    )

encrypt_procs = []
hash_procs = []

for _ in range(5):
    data = os.urandom(10)

    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)

    # once comment out 2 lines below
    # encrypt_proc communicate return '', except the last
    hash_proc = run_hash(encrypt_proc.stdout)
    hash_procs.append(hash_proc)

for encrypt_proc in encrypt_procs:
    print('encrypt_proc.communicate', encrypt_proc.communicate())
    assert encrypt_proc.returncode == 0

for hash_proc in hash_procs:
    print('hash_proc.communicate', hash_proc.communicate())
    assert hash_proc.returncode == 0

