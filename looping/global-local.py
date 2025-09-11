print('Belajar global dan local')

# variabel global
x = 10

def contoh():
    # variabel local
    x = 5
    print("Print X dari local", x)

contoh()
print("Print X dari global", x)