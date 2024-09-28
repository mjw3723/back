while True:
    arr = []
    n = int(input())
    if n == -1 :
        break
    
    for i in range(n):  # 약수 구하기
        if n % (i+1) == 0:
            arr.append(i+1)
    r = 0
    for i in range(int(len(arr)-1)): # 약수들의 합
        r += arr[i]
        
    result = str(n)+" = " 
    if r == arr[len(arr)-1]:
        for i in range(int(len(arr)-1)):
            if i == len(arr)-2:
                result += str(arr[i])
            else:
                result += str(arr[i])+" + "
        print(result)   
    else:
        print(str(n)+" is NOT perfect.")