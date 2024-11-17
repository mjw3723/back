from collections import deque 
import sys

N = int(sys.stdin.readline())
queue = deque([])
for i in range(N):
    M = sys.stdin.readline().strip()
    if M.startswith("1") or M.startswith("2"):
        cmd , value = M.split()
        if cmd == "1":
            queue.appendleft(int(value))
        elif cmd == "2":
            queue.append(int(value))
    if M == "3":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if M == "4":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    if M == "5":
        print(len(queue))
    if M == "6":
        if queue:
            print(0)
        else:
            print(1)
    if M == "7":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if M == "8":
        if queue:
            print(queue[-1])
        else:
            print(-1)