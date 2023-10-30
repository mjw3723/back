N = int(input())
strings = []

# 문자열 입력 받기
for _ in range(N):
    strings.append(input())

result = ''
for i in range(len(strings[0])):
    char = strings[0][i]  # 첫 번째 문자를 기준으로 설정
    for j in range(1, N):
        if strings[j][i] != char:
            char = '?'
            break
    result += char
    
print(result)
