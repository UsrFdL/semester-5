nilai = int(input('nilai: '))

if nilai > 100:
    print('Nilai invalid')
elif nilai > 80:
    print('A')
elif nilai > 75:
    print('B+')
elif nilai > 69:
    print('B')
elif nilai > 60:
    print('C+')
elif nilai > 55:
    print('C')
elif nilai > 50:
    print('D+')
elif nilai > 44:
    print('D')
elif nilai > 0:
    print('E')
else:
    print('Nilai invalid')
    