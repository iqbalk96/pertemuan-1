nama = input("Nama: ")
umur = int(input("Umur: "))
tinggi = float(input("Tinggi: "))

print("\n=== Hasil Input ===")
print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Tinggi: {tinggi}")

if umur >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda belum dewasa test")