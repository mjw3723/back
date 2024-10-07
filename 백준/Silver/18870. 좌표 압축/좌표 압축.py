import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
S = list(set(arr))
S.sort()
ans = {}
for i in range(len(S)):
    ans[S[i]] = i
print(" ".join(str(ans[i])for i in arr))