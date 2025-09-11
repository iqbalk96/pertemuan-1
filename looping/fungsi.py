# fungsi
def sapa():
    print("Halo, Selamat malam")

sapa()

# parameter dan return
def penjumlahan(a, b, c):
    # logic
    return (a - b) * c

# variabel
hasil = penjumlahan(7, 2, 2)
print(hasil)

def desimalPenjumlahan(d, e=0):
    return d + e

hasilDesimalPenjumlahan = desimalPenjumlahan(1.2, 1.3)
print(hasilDesimalPenjumlahan)

def stringWithParam(f="Selamat malam dari default"):
    return f

hasilString = stringWithParam("Selamat malam dari parameter")
print(hasilString)

