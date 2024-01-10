T = int(input())
p = [0,1]

for i in range(19):
    p.append(p[i] + p [i+1])
    

print(p[T])