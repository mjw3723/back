def number(x):
    if x == 1 : return False
    for i in range(2,x):
        if x % i ==0:
            return False
    
    return True

N = input()
num_list = list(map(int, input().split()))
cnt = 0
for i in range(len(num_list)):
    if number(num_list[i]):
        cnt +=1
        
print(cnt)