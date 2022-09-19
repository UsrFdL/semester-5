nilai = int(input('nilai: '))

if nilai < 0:
    print("Nilai invalid")
if nilai >= 0 and nilai <= 44:
    print("E")
if nilai > 44 and nilai <= 50:
    print("D")
if nilai > 50 and nilai <= 55:
    print("D+")
if nilai > 55 and nilai <= 60:
    print("C")
if nilai > 60 and nilai <= 69:
    print("C+")
if nilai > 69 and nilai <= 75:
    print("B")
if nilai > 75 and nilai <= 80:
    print("B+")
if nilai > 80 and nilai <= 100:
    print("A")
if nilai > 100:
    print("Nilai invalid")