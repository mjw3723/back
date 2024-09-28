import sys
n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
print('\n'.join(str(i)for i in arr))