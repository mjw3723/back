import sys
input = sys.stdin.readline
D = {}
N = int(input().strip())
arr = list(map(int,input().split(" ")))
for i in arr:
    if D.get(i):
        D[i] = D[i]+1
    else:
        D[i] = 1
M = int(input())
ans = list(map(int,input().split(" ")))
for i in ans:
    if D.get(i):
        print(D[i],end=" ")
    else:
        print('0',end=" ")