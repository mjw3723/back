import sys
N = int(sys.stdin.readline().strip())
Q = []
for i in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        Q.append(cmd[1])
    elif cmd[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(Q))
    elif cmd[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'pop':
        if Q:
            print(Q.pop(0))
        else:
            print(-1)