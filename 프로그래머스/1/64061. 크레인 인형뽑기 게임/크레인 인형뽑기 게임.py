def solution(board, moves):
    # 각열에 대한 스택을 생성
    stack = [[] for _ in range(len(board[0]))]
    # board 역순으로 탐색, 각열의 인형을 stack에 추가
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                stack[j].append(board[i][j])
    bucket = [] # 인형 담을 리스트
    answer = 0  #사라진 인형 개수
    # moves 를 순회, 각열에서 인형을 뽑아 bucket에 추가
    for m in moves:
        if stack[m-1]: # 해당 열에 인형이 있는 경우
            doll = stack[m-1].pop()
            
            if bucket and bucket[-1] == doll: # 바구니에 인형이 있고, 가장 위에 있는 인형과 같은경우
                bucket.pop()
                answer+=2
            else: # 바구니에 인형이 없거나 , 가장위에 있는 인형과 다른 경우
                bucket.append(doll)
    return answer
