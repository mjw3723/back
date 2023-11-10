N,M = input().split(" ")

X = N[::-1]
Y = M[::-1]

Rev = int(X) + int(Y)

result = str(Rev)[::-1]

print(int(result))