from collections import deque
def solution(cards1, cards2, goal):
    cards1, cards2, goal = map(deque, [cards1, cards2, goal])
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
            continue
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
            continue
        break
    return "Yes" if not goal else "No"