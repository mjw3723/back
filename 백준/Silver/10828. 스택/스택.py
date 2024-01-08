import sys
T = int(sys.stdin.readline())
result = []
for _ in range(T):
    word = sys.stdin.readline().split()
    if word[0] =='push':
        result.append(word[1])
    elif word[0] =='pop':
        if len(result)==0:
            print(-1)
        else:
            print(result.pop())
    elif word[0] == 'size':
        print(len(result))
    elif word[0] == 'empty':
        if len(result) == 0 :
            print(1)
        else : print(0)
    elif word[0] == 'top':
        if len(result) == 0:
            print(-1)
        else: print(result[-1])   
    