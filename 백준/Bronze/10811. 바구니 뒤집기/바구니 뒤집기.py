N,M = map(int,input().split(' '))
arr = [i+1 for i in range(N)]
for _ in range(M):
    i,j = map(int,input().split(' '))
    r = list(reversed(arr[i-1:j]))
    for k in range(i-1,j):
        arr[k] = r.pop(0)
    
print(" ".join(map(str,arr)))