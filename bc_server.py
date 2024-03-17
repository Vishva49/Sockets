from subprocess import Popen, STDOUT, PIPE
from threading import Thread

p = Popen(['bc','-q'],stderr=STDOUT,stdin=PIPE,stdout=PIPE)
#p.stdin.write(b"1+2")
#p.stdin.flush()
#p.stdout.readline()

while True:
    cmd = input()
    if cmd != 'quit':
        cmd = cmd + "\n"
        p.communicate(cmd.encode())
        p.stdout.readline()
    else:
        break