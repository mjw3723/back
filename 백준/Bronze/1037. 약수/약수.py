N = int(input())

numbers = list(map(int, input().split()))
max = max(numbers)
min = min(numbers)

result = max*min
print(result)
