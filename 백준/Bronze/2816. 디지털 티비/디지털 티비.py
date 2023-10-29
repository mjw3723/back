#1.화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
#2.화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
#3.현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
#4.현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)
N = int(input())
List = []
result = ''
temp = ''
for i in range(N):
    List.append(str(input()))
     
for i in range(len(List)):
    if List[0] == 'KBS1':
        break
    if List[i] != 'KBS1':
        result += '1'
    if List[i] == 'KBS1':
        for j in reversed(range(i+1)):
            if j == 0:
                break
            temp = List[j-1]
            List[j-1] = List[j]
            List[j] = temp
            result += '4'
temp = ''
for i in range(len(List)):
    if List[1] == 'KBS2':
        break
    if List[i] != 'KBS2':
        result += '1'
    if List[i] == 'KBS2':
        for j in reversed(range(i+1)):
            if j == 1:
                break
            temp = List[j-1]
            List[j-1] = List[j]
            List[j] = temp
            result += '4'
       
print(result)

         