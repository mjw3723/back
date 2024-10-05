from collections import deque

n , k = map(int,input().split(" "))
q = deque([int(i+1) for i in range(n)])
ans = '<'

while q:
    for i in range(k):
        if i != k-1:
            q.append(q.popleft())
        if i == k-1:
            if len(q) > 1:
                ans += str(q.popleft())+", "
            else:
                ans += str(q.popleft())
                
ans += '>'
print(ans)