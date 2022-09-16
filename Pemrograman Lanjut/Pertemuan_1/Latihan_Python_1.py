"""
Ubahlah kode di bawah sehingga bila program dijalankan pada hari Sabtu atau Minggu akan menampilkan tulisan HARI LIBUR,
sedangkan bila program dijalankan pada hari lainnya akan menampilkan tulisan HARI KERJA
"""

from datetime import date
import calendar

libur = ["Saturday", "Sunday"]

curr_date = date.today()
if calendar.day_name[curr_date.weekday()] in libur:
    print("HARI LIBUR")
else:
    print("HARI KERJA")