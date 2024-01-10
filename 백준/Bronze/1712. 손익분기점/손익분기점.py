A,B,C = map(int,input().split())
if C > B:
    result = (A // abs(B-C))+1
    print(result)
else :print(-1)