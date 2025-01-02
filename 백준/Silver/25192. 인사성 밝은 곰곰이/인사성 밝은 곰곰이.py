N = int(input())
count = 0
arr = set()
for _ in range(N):
    n = input()
    if n != 'ENTER':
        if n not in arr:
            count+=1
            arr.add(n)
    else:
        arr.clear()
print(count)
    