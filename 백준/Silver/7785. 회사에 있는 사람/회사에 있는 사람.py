N = int(input())
d = {}
for i in range(N):
    name, state = input().split(" ")
    if state == 'leave':
        d.pop(name)
        continue
    d[name] = state
a = sorted(d,reverse=True)
for i in a:
    print(i)