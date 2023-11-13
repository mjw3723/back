import datetime

M,D = input().split()
M=int(M)
D=int(D)

week = datetime.date(2007,M,D).weekday()

if week == 0:
    print('MON')
elif week ==1:
    print('TUE')
elif week == 2:
    print('WED')
elif week == 3:
    print('THU')
elif week == 4:
    print('FRI')
elif week == 5 :
    print('SAT')
elif week == 6 :
    print('SUN')