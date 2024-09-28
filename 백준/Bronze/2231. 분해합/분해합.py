n = int(input())
result = 0
for i in range(n):
    arr = list(str(i))
    sum = 0
    for j in range(int(len(arr))):
        sum += int(arr[j])
    if int(i) + int(sum) == n:
        result = i
        break

print(result)