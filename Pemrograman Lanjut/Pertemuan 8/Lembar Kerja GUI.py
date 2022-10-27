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
tk.geometry("400x100")
frame = Frame(tk)
frame.grid(row=1)
lbl_0 = Label(tk, text="Masukkan kata dalam bahasa inggris yang akan diterjemahkan: ")
lbl_0.grid(row=0, sticky=W)
lbl_1 = Label(frame, text="English - Indonesia : ")
lbl_1.grid(row=0, pady=5, sticky=W)
entry_1 = Entry(frame, bd=2, width=35)
entry_1.grid(row=0, column=1, pady=5, sticky=W)
btn_1 = Button(frame, text="Translate", command=printInput, padx=5)
btn_1.grid(row=0, column=2, pady=5)
lbl_2 = Label(frame, text="Result : ")
lbl_2.grid(row=1, sticky=E)
terjemahan = Listbox(frame, height=1, width=35, bd=2)
terjemahan.grid(row=1, column=1, sticky=W)
tk.mainloop()
