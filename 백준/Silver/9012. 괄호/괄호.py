T = int(input())

for _ in range(T):
    word = input()
    cnt = 0
    for i in range(len(word)):
        if word[i] =='(':
           cnt +=1
        elif word[i] == ')':
            cnt -=1
        
        if cnt ==0:
            result ='YES'
        elif cnt ==-1:
            result = 'NO'
            break
        else :
            result = 'NO'
    print(result)