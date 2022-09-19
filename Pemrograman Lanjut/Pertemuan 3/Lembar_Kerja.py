isi_data = open('data.txt', 'a')
data = input("Masukkan kalimat yang akan disimpan: ")
isi_data.write(data + "\n")
isi_data.close
print("Terima kasih. Kalimatmu telah disimpan pada file data.txt")