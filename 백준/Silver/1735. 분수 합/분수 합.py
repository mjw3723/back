import sys
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def simplify_fraction(numerator, denominator):
    while True:
        gcd_value = gcd(numerator, denominator)
        if gcd_value == 1:  
            break
        numerator //= gcd_value
        denominator //= gcd_value
    return numerator, denominator
input = sys.stdin.readline
N1 , M1 = map(int,input().split())
N2 , M2 = map(int,input().split())
ans = 0
if M1 == M2 :
    M = M1
    ans = N1+N2
else:
    M = M1 * M2
    N1 = M2 * N1
    N2 = M1 * N2
    ans = N1+N2
ans , M = simplify_fraction(ans, M)
print(str(ans)+" "+str(M))