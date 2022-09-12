n = int(input('masukkan bilangan bulat positif: '))
jumlah = 0

for i in range(1, n+1):

    if i%2 == 0:
        jumlah += i

print('Jumlah ' + str(n) + ' bilangan bulat genap pertama adalah: '+ str(jumlah))