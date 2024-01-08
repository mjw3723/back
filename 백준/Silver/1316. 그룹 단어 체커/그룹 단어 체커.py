T = int(input())
result=0
for _ in range(T):
    text = input()
    no = 0
    for i in range(len(text)-1):
        if text[i] != text[i+1]:
          new = text[i+1:]
          if new.count(text[i])>0:
              no+=1
    if no == 0:
        result+=1
print(result)  