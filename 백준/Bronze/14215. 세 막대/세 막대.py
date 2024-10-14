import sys
a,b,c = map(int,sys.stdin.readline().split())

if a >= b+c :
    a = a - (abs((b+c)-a)+1)
elif b >= a+c:
    b = b - (abs((a+c)-b)+1)
elif c >= a+b:
    c = c - (abs((a+b)-c)+1)
print((a+b+c))