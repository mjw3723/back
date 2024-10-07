N = int(input())
arr = []
for _ in range(N):
    X, Y = map(int,input().split(" "))
    tu = (X, Y)
    arr.append(tu)
arr.sort(key=  lambda x : (x[0],x[1]))

for i in range(len(arr)):
    print(str(arr[i][0])+" "+str(arr[i][1]))