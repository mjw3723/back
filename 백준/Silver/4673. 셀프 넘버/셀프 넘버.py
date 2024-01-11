N = set(range(1,10000))
remove = set()
for i in N:
    for j in str(i):
        i += int(j)
    remove.add(i)

number = N - remove
for n in sorted(number):
    print(n)