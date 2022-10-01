rpt = int(input("Jumlah angka genap yang ingin disimpan: "))
count = 1

while count <= rpt:
    inp = int(input("Masukkan angka: "))
    if inp % 2 == 0:
        count += 1
        print(inp)
    else:
        print("Bukan angka genap!")
    print()