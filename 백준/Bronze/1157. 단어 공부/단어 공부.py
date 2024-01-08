T = input()
Tu = T.upper()
cnt = 0
result = ''
a = list(set(Tu))

for i in range(len(a)):
    if Tu.count(a[i])>cnt:
        cnt = Tu.count(a[i])
        result = a[i]
    elif Tu.count(a[i])==cnt:
        result = '?'

print(result)  