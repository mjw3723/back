def solution(record):
    answer = []
    chat = {}
    for i in record:
        if i.startswith('Enter') or i.startswith('Change'):
            chat[i.split()[1]] = i.split()[2]
    for i in record:
        if i.startswith('Enter'):
            answer.append(chat[i.split()[1]]+"님이 들어왔습니다.")
        elif i.startswith('Leave'):
            answer.append(chat[i.split()[1]]+"님이 나갔습니다.")
    return answer