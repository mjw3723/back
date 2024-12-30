import sys
input = sys.stdin.readline
N , M = map(int,input().split())
D = {}
R = {}
for i in range(1,N+1):
    S = input().rstrip()
    D[S] = i
    R[i] = S
for i in range(M):
    A = input().rstrip()
    if A.isdigit():
        print(R[int(A)])
    elif A.isalpha():
        print(D[A])