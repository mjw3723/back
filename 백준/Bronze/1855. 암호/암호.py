N = int(input())
M = str(input())

arr = []
list = []
result = ''
for char in M: 
    arr.append(char)

for i in range(int(len(M)/N)):
    if int(i % 2) == 0:
        list.append(arr[i*N:(i+1)*N])
    elif int(i % 2) == 1:
        list.append(arr[i*N:(i+1)*N][::-1])
for j in range(N):        
    for i in range(len(list)):
        result += list[i][j]

print(result)
