def solution(participant, completion):
    dic = {}
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    for c in completion:
        dic[c] -= 1
    
    for k in dic.keys():
        if dic[k] > 0:
            return k