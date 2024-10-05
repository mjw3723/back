import sys
from collections import deque
queue = deque([int(i+1) for i in range(int(sys.stdin.readline()))])
while queue:
    num = queue.popleft()
    if len(queue) == 0:
        print(num)
        break
    queue.append(queue.popleft())