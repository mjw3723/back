N,M = map(int,input().split())
ball = [i+1 for i in range(N)]

for _ in range(M):
    A,B = map(int,input().split())
    temp = ball[B-1]
    ball[B-1] = ball[A-1]
    ball[A-1] = temp
    
for i in range(len(ball)):
    print(ball[i],end=' ')