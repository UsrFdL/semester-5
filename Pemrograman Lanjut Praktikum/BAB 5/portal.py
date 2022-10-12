import csv
import os

fieldname = ["username" ,"password", "hakAkses"]

with open("user.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldname)

    writer.writeheader()
    writer.writerow({"username":"user", "password": "user123","hakAkses": 0})
    writer.writerow({"username":"admin","password": "admin123","hakAkses": 1})

if not os.path.exists("hello.txt"):
    with open("hello.txt", "w", newline="") as file:
        file.write("Welcome to dashboard")
        
while True:
    inp = int(input("1. Login\n2. Registrasi\n3. Keluar\n-> "))
    if inp == 1:
        print("\nLogin\n" + "-"*33)
        username = input("Username: ")
        password = input("Password: ")
        with open("user.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if username == row["username"] and password == row["password"]:
                    available = True
                    akses = int(row["hakAkses"])
                    break
        if available:
            if akses:
                with open("hello.txt", "r") as file:
                    print("\nAdmin\n" + "-"*33+ "\n" + file.read())
                pil = int(input("\n1. Edit\n2. Kembali\n-> "))
                if pil == 1:
                    kata = input("masukkan kalimat sambutan: ")
                    with open("hello.txt", "w", newline="") as file:
                        file.write(kata)
                    print(f"Kata sambutan telah diubah menjadi \"{kata}\"")
                elif pil == 2:
                    print("\n\n")
                    continue
            else:
                with open("hello.txt", "r") as file:
                    print("\nGuest\n" + "-"*33+ "\n" + file.read())
        else:
            print("username atau password yang anda masukkan salah")
    elif inp == 2:
        print("\nRegistrasi\n" + "-"*33)
        username = input("Username: ")
        password = input("Password: ")
        buat = True
        ganda = False
        with open("user.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if username == row["username"]:
                    ganda = True
                    print("username telah digunakan")
                    break
        if not ganda:
            pil = int(input("1. guest\n2. admin\n-> "))
            akses = 0
            if pil == 2:
                verifikasi = input("Kode verifikasi: ")
                if verifikasi == "iamgod":
                    akses = 1
                else:
                    print("Gagal membuat akun, kode verifikasi salah")
                    buat = False
            if buat:
                with open("user.csv", "a", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldname)
                    writer.writerow({"username":username, "password": password,"hakAkses": akses})
                if akses == 1:
                    print("Berhasil registrasi sebagai admin")
                else:
                    print("Berhasil registrasi sebagai guest")
    elif inp == 3:
        break
    input("\npress ENTER to continue...")
    print("\n\n")