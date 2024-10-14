import sys
x, y, w, h = map(int,sys.stdin.readline().split(" "))
x1 = abs(x - w)
x2 = abs(0 - min(x,w))
y1 = abs(y - h)
y2 = abs(0 - min(y,h))
print(min(min(x1,x2),min(y1,y2)))