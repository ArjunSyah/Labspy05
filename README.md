# Labspy05
# Latihan1
## Membuat daftar kontak dengan menggunakan dicctionary pada python
### Berikut Programnya
![gambar1](ss/s0.PNG)
- Dengan keterangan
```python
daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Arjun Syah":"0855915297998", "Siti Nuraisah":"085287997552"}
```
- diatas adalah untuk menampung data dari kamus
### kondisi 1
```python
print("="*50)
print("   Nama              |    Nomor Telepon   " )
print("="*50)
print(" # Arjun Syah        |   ", kontak["Arjun Syah"])
print(" # Siti Nuraisah     |   ", kontak["Siti Nuraisah"])
print("-"*50)
print()
print()
print("="*50)
```
- untuk mengakses atau menampilkan kontak yang telah ditampung dalam kamus
### Berikut hasil dari programnya
![gambar2](ss/s1.PNG)
### kondisi 2
```python
print("Menampilkan Kontak Arjun Syah")
print("="*50)
print(" # Arjun Syah        |   ", kontak["Arjun Syah"])
print("-"*50)
print()
print()
print("="*50)
```
- Kode diatas adalah untuk menampilkan salah satu daftar kontak yang ada
### Berikut hasil programnya
![gambar3](ss/s2.PNG)
### Kondisi 3
```python
print("Menambahkan kontak dengan Nama Haikal")
print("dengan Nomor telepon 085215376070")
kontak["Haikal"]="085215376070"
print("="*50)
print(" # Haikal            |   ", kontak["Haikal"])
print("-"*50)
print()
print()
print("="*50)
```
- kode diatas untuk menambahkan konntak 
### Berikut hasil programnya
![gambar4](ss/s3.PNG)
### kondisi 4
```python
print("Mengubah Nomor Siti Nuraisah dengan Nomor 08521267890")
print("="*50)
print(" # Siti Nuraisah     |    ", kontak["Siti Nuraisah"])
print("-"*50)
print()
print()
print("="*50)
```
- Kode diatas untuk mengubah kontak
### Berikut hasil programnya
![gambar5](ss/s4.PNG)
### Kondisi 5
```python
print("Menampilkan semua Nomor dalam Konntak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)
```
- kode diatas adalah untuk menampilkan semua nomor yang ada
### Berikut hasil programnya
![gambar6](ss/s5.PNG)
### kondisi 6
```python
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)
```
- Kode diatas adalah untuk menampilkan semua daftar dalam kontak
### Berikut hasil programnnya
![gambar7](ss/ss6.PNG)
### Kondisi 7
```python
print("Hapus Kontak Haikal")
print("="*50)
kontak.pop("Haikal") 
print(kontak.items())
print("-"*50)
print()
print()
```
- kode di atas adalah untuk menghapus salah satu dari konntak yang ada
### Berikut hasil programnya
![gambar8](ss/s7.PNG)
## latihan1 selesai
