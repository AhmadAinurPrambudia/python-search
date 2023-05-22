def sequential_search(phonebook, name):
    for entry in phonebook:
        if entry[0] == name:
            return entry[1]
    
    return "Nomor telepon tidak ditemukan."

# Buku telepon
phonebook = [
    ("John Doe", "081234567890"),
    ("Jane Smith", "089876543210"),
    ("Michael Johnson", "087811223344"),
    ("Emily Davis", "082122232425")
]

# Meminta input nama yang ingin dicari nomor teleponnya
name = input("Masukkan nama yang ingin Anda cari nomor teleponnya: ")

# Mencari nomor telepon menggunakan sequential search
number = sequential_search(phonebook, name)

# Menampilkan hasil
print("Nomor telepon", name, "adalah:", number)
