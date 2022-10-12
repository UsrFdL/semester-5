teks = input("Masukkan data diri anda:\ncontoh: (Nama:Ucup,NIM:123,dst.)\ninput: ")

key = []
value = []
tmp = ""

for i in teks:
    if i == ":":
        key.append(tmp)
        tmp = ""
        continue
    elif i == ",":
        value.append(tmp)
        tmp = ""
        continue
    tmp += i
value.append(tmp)

print()
for i in range(len(key)):
    print(f"{key[i]} Anda: {value[i]}")