n = int(input())
arr = [str(input()) for _ in range(n)]
se = list(set(arr))
se.sort()
se.sort(key=len)
print("\n".join(str(i) for i in se))