import sys 

N = sys.stdin.readline()
stack = []
for i in range(int(N)):
    M = sys.stdin.readline()
    if len(M) > 2 :
        a , b = map(int,M.split(" "))
    else:
        a = M
    if a == 1 :
        stack.append(b)
    elif int(a) == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif int(a) == 3:
        print(len(stack))
    elif int(a) == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif int(a) == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)