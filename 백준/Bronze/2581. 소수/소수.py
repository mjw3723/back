M = int(input())
N = int(input())

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True
result = []
state = 0 
for i in range(M,N+1):
    if(isPrime(i)):
        result.append(i)
        state = 1

if state :
    print(sum(result))
    print(min(result))
else :
    print(-1)