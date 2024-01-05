num_list = list(map(str, input().split()))
result = []
for i in range(len(num_list)):
    result.append(num_list[i][::-1])
    
if int(result[0]) > int(result[1]):
    print(result[0])
else: print(result[1])