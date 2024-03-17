from subprocess import Popen, STDOUT, PIPE
from threading import Thread

class outputProcessThread(Thread):
    def __init__(self,p):
        Thread.__init__(self)
        self.p = p
    def run(self):
        while self.p.poll() is None:
            print("waiting for result")
            print(self.p.stdout.readline().decode())

p = Popen(['bc','-q'],stderr=STDOUT,stdin=PIPE,stdout=PIPE)
#p.stdin.write(b"1+2")
#p.stdin.flush()
#p.stdout.readline()
out = outputProcessThread(p)
out.start()
while p.poll() is None:
    cmd = input()
    if cmd != 'quit':
        cmd = cmd + "\n"
        p.stdin.write(cmd.encode())
        p.stdin.flush()
    else:
        break