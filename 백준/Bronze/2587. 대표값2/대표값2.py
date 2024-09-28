arr = [int(input()) for _ in range(5)]
arr.sort()
s = 0
for i in range(5):
    s += arr[i]
    avg = s//5
print(avg)
print(arr[len(arr)//2])