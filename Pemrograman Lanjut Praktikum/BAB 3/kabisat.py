tahun = int(input("Tahun: "))
kabisat = True if tahun % 4 == 0 and tahun % 100 == 0 and tahun % 400 == 0 else False
if kabisat:
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")