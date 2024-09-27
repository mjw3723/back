case = int(input())
arr = [int(input()) for _ in range(case)]

for i in range(int(len(arr))):
    q,d,n,p = 0,0,0,0
    if arr[i] // 25 > 0 : #쿼터
        q = arr[i] // 25
        arr[i] = arr[i] - (q*25)
    
    if arr[i] // 10 > 0: #다임
        d = arr[i] // 10
        arr[i] = arr[i] - (d*10)
    
    if arr[i] // 5 > 0 : # 니켈
        n = arr[i] // 5
        arr[i] = arr[i] - (n*5)
        
    if arr[i] // 1 > 0 : #페니
        p = arr[i] // 1

    print(str(q) + " " + str(d) + " " + str(n) + " " + str(p))