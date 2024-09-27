result = [input() for i in range(5)]


for i in range(15):
    for j in range(5):
        if i < len(result[j]):
            print(result[j][i],end='')