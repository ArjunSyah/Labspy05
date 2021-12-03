daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Arjun Syah":"0855915297998", "Siti Nuraisah":"085287997552"}

print("="*50)
print("   Nama              |    Nomor Telepon   " )
print("="*50)
print(" # Arjun Syah        |   ", kontak["Arjun Syah"])
print(" # Siti Nuraisah     |   ", kontak["Siti Nuraisah"])
print("-"*50)
print()
print()
print("="*50)

# Menampilkan kontak Arjun Syah
print("Menampilkan Kontak Arjun Syah")
print("="*50)
print(" # Arjun Syah        |   ", kontak["Arjun Syah"])
print("-"*50)
print()
print()
print("="*50)

# Menambahkan kontak dengna nama haikal 
print("Menambahkan kontak dengan Nama Haikal")
print("dengan Nomor telepon 085215376070")
kontak["Haikal"]="085215376070"
print("="*50)
print(" # Haikal            |   ", kontak["Haikal"])
print("-"*50)
print()
print()
print("="*50)

# Mengubah Nomor Siti Nuraisah dengan Nomor baru
print("Mengubah Nomor Siti Nuraisah dengan Nomor 08521267890")
print("="*50)
print(" # Siti Nuraisah     |    ", kontak["Siti Nuraisah"])
print("-"*50)
print()
print()
print("="*50)


# Menampilkan semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.keys())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan semua Nomor
print("Menampilkan semua Nomor dalam Konntak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan semua daftar kontak
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)


# Menghapus Salah satu Kontak
print("Hapus Kontak Haikal")
print("="*50)
kontak.pop("Haikal") 
print(kontak.items())
print("-"*50)
print()
print()



