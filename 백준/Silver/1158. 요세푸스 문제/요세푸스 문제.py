from collections import deque
N , K = map(int,input().split(" "))

arr = deque([N+1 for N in range(N)])

ans = []

while arr:
    for i in range(K):
        x = arr.popleft()
        if i == (K-1):
            ans.append(str(x))
        else:
            arr.append(x)

print("<{}>".format(', '.join(ans)))