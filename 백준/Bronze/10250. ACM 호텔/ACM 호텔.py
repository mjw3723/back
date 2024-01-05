T = int(input())
n_list=[]
result = ''

for i in range(T):
    h,w,n = list(map(int,input().split()))
    f = n % h
    r = (int(n//h)+1)
    if f == 0:
        f = h
        r -= 1
    print(f * 100 + r)