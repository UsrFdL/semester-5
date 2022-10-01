teks = ["Tinggi", "Lebar", "Ketebalan huruf"]
bil = []
for i in range(3):
    x = int(input(f"{teks[i]}: "))
    bil.append(x)
for i in range(bil[0]):
    for j in range(bil[1]):
        if i >= bil[2] and j >= bil[2] and i < bil[0] - bil[2]:
            print("-", end="")
        else:
            print("*", end="")
    print("\n")