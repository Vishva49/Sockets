from subprocess import Popen, STDOUT, PIPE
from threading import Thread

def getoutput(p):
    while p.poll() is None:
        print(p.stdout.readline().decode().strip())

p = Popen(['bc','-q'],stderr=STDOUT,stdin=PIPE,stdout=PIPE)
#p.stdin.write(b"1+2")
#p.stdin.flush()
#p.stdout.readline()

t = Thread(target=getoutput, args=(p,))
t.start()
while p.poll() is None:
    cmd = input()
    cmd = cmd + "\n"
    p.stdin.write(cmd.encode())
    p.stdin.flush()