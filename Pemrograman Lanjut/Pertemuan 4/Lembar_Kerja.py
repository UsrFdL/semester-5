kata = str(input("Masukkan kata dalam bahasa inggris yang akan diterjemahkan: "))
kamus = {
    "fish": "ikan",
    "car": "mobil",
    "phone": "telepon"
}
if kata in kamus:
    print(kata + "artinya adalah: " + kamus[kata])
else:
    print("maaf, terjemahan belum ditemukan.")