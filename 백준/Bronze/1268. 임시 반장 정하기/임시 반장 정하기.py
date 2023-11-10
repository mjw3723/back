N = int(input())
S_list = []
c_list = [0]*N
for i in range(N):
    S_list.append(list(map(int, input().split())))
    c_list[i] = [0]*N

for i in range(5):
    for j in range(N):
        for k in range(j+1,N):
            if S_list[j][i] == S_list[k][i]:
                c_list[k][j] = 1
                c_list[j][k] = 1
                
cnt = []
for c in c_list:
    cnt.append(c.count(1))
    
print(cnt.index(max(cnt))+1)
                