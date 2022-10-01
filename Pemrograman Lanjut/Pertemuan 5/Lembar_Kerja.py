def hitungLuas(*sisi):
    if len(sisi) == 1:
        l = sisi[0]*sisi[0]
    elif len(sisi) == 2:
        l = sisi[0]*sisi[1]
    elif len(sisi) == 3:
        s = 0.5 * (sisi[0] + sisi[1] + sisi[2])
        l = (s*(s-sisi[0])*(s-sisi[1])*(s-sisi[2]))**0.5
    else:
        return "invalid data"
    return l

print(hitungLuas(2)) #menghitung luas persegi dengan sisi 2
print(hitungLuas(3, 4)) #menghitung luas persegi panjang dengan panjang 3 dan lebar 4
print(hitungLuas(5, 6, 7)) #menghitung luas segitiga dengan panjang sisi-sisinya 5, 6, dan 7