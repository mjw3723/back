import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    age , name = map(str,sys.stdin.readline().split())
    age = int(age)
    arr.append([age,name])
arr.sort(key= lambda x : (x[0]))

for i in arr:
    print(i[0], i[1])