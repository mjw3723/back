def fect(n):
    if(n>1):
        return n * fect(n-1)
    else:
        return 1

N = int(input())
print(fect(N))