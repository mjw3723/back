D = str(input())

cnt = 0
for i in range(len(D)):
    if int(ord(D[i])) >=65 and int(ord(D[i]))<=67 :
        cnt +=3
    elif int(ord(D[i])) >=68 and int(ord(D[i]))<=70: 
        cnt+=4
    elif int(ord(D[i])) >=71 and int(ord(D[i]))<=73:  
        cnt+=5
    elif int(ord(D[i])) >=74 and int(ord(D[i]))<=76:
        cnt +=6
    elif int(ord(D[i])) >=77 and int(ord(D[i]))<=79:
        cnt +=7
    elif int(ord(D[i])) >=80 and int(ord(D[i]))<=83:
        cnt +=8
    elif int(ord(D[i])) >=84 and int(ord(D[i]))<=86:
        cnt +=9
    elif int(ord(D[i])) >=87 and int(ord(D[i]))<=90:
        cnt +=10  
    
print(cnt) 