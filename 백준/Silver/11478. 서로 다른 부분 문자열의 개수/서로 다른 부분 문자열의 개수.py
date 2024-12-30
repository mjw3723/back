a = input()
S = set()
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        S.add(a[i:j])
    
print(len(S))