arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int,input().split())
answer = ''
while n :
    answer = arr[n % b] + answer
    n //= b
print(answer)