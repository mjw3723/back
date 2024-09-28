n, m = map(int,input().split())
arr = []
for i in range(n):
    if n % (i+1) == 0 :
        arr.append(i+1)
if (m) > len(arr):
    print(0)
else:
    print(arr[m-1])