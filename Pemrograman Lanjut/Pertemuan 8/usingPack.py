from tkinter import *

def Kamus(kata):
    kamus = {
        "fish": "ikan",
        "car": "mobil",
        "phone": "telepon"
    }

    if kata in kamus:
        return (kata + " artinya adalah: " + kamus[kata])
    else:
        return ("maaf, terjemahan belum ditemukan")

def printInput():
    inp = Kamus(entry_1.get())
    terjemahan.delete(first=0, last=None)
    terjemahan.insert(1, inp)

tk = Tk()
tk.title("Translator")
tk.geometry("350x100")

baris_1 = Frame(tk)
baris_1.pack(side=TOP, anchor=W)
baris_2 = Frame(tk)
baris_2.pack(side=TOP, anchor=W)
baris_3 = Frame(tk)
baris_3.pack(side=TOP, anchor=W)
baris_4 = Frame(tk)
baris_4.pack(side=TOP, anchor=W)

lbl_1 = Label(baris_1, text="Masukkan kata dalam bahasa inggris yang akan diterjemahkan: ")
lbl_1.pack(side=LEFT, padx=2)
entry_1 = Entry(baris_2, bd=2, width=35)
entry_1.pack(side=LEFT, padx=5)
btn_1 = Button(baris_2, text="Translate", command=printInput)
btn_1.pack(side=LEFT, padx=5)
lbl_2 = Label(baris_3, text="Result : ")
lbl_2.pack(side=LEFT, padx=2)
terjemahan = Listbox(baris_4, height=1, width=35, bd=2)
terjemahan.pack(side=LEFT, padx=5)

tk.mainloop()