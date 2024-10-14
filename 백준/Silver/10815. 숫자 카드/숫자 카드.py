N = int(input())
sang = list(map(int,input().split(" ")))
dic = {}
M = int(input())
card = list(map(int,input().split(" ")))
for i in range(M):
    dic[card[i]] = 0

for i in range(N):
    dic[sang[i]] = 1
    
print(" ".join(str(dic[i]) for i in card))