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
# Menampilkan semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.keys())
print("-"*50)
print()
print()
print("="*50)
```
- kode diatas untuk menampilkan semua nama dalam daftar kontak
### Berikut hasil programnya
![gambar6](ss/s5.PNG)
### Kondisi 6
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
![gambar7](ss/s6.PNG)
### kondisi 7
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
![gambar8](ss/s7.PNG)
### Kondisi 8
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
![gambar9](ss/s8.PNG)
## latihan1 selesai
============================================================================

# Praktikum 5
## Membuat program input data nilai siswa dengan menerapkan menu tambah, ubah,cari, hapus dan keluar
### Flowchart
![gambar10](ss/s9.png)
### Berikut Programnya
![gambar11](ss/s10.PNG)
### Dengan keterangann
```python
a = {}
```
- Kode diatas untuk membuat dictionary kosong, untuk menampung dictionary dengan mrnggunakan tuple
```python
while True:
    x = input ("[T]tambah, [U]ubah, [H]hapus, [C]cari, [L]lihat, [K]keluar: ")
```
- kode diatas untuk perulangan while, dan juga untuk menginisialkan penambahanan menu pilihan yaitu Tambah, Ubah, Hapus, Cari, Lihat dan Keluar
```python
if x.lower() == "t":
        print("Ubah Data")
        nama = input("Masukan Nama               : ")
        nim = int(input("Masukan NIM                : "))
        uts = int(input("Nilai UTS                  : "))
        uas = int(input("Nilai UAS                  : "))
        tugas = int(input("Nilai Tugas                : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a[nama] = nim, uts, uas, tugas, hasil
```
- kode diatas untuk syntak penambahan data, jika mengetikan "t" artinya menambahkan data, dan ditampung kedalam dictionary "a={}" dengan status keys, dan yang lainnya sebagai values
```python
elif x.lower() == "u":
        print("Ubah Data")
        nama = input("Masukan Nama              : ")
        if nama in a.keys():
            nim = int(input("Masukan NIM                : "))
            uts = int(input("Nilai UTS                  : "))
            uas = int(input("Nilai UAS                  : "))
            tugas = int(input("Nilai Tugas                    : "))
            hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35                
            a[nama] = nim, uts, uas, tugas, hasil
        else:
            print("Nama{0} Tidak di Tentukan".format(nama))
```
- code diatas untuk syntax mengubah data, jika mengetikan "u" maka akan melakukan perubahan data, tetapi yang dapat dibah hanya valuesnya saja
```python
 elif x.lower() == "h":
        print("Hapus Data")
        nama = input("Masukan Nama              : ")    
        if nama in a.keys():
            del a[nama]
        else:
            print("Nama{0} Tidak di Temukan".format(nama))
```
- code diatas untuk syntak menghapus data, jika mengetikan "h" maka akaan melakukan penghapusan dengan statemen "del a[nama]"
```python
elif x.lower() == "c" :
        print("Cari Data")            
        nama = input("Masukan Nama              : ")
        if nama in a.keys():
            print("="*75)
            print("|                                   DAFTAR MAHASISWA                                   ") 
            print("="*75)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |" 
                 .format(nama, nim, uts, uas, tugas,hasil))
            print("="*75)
        else:
            print("Nama{0} Tidak di Tentukan".format(nama))
```
- code diatas adalah syntak untuk pencarian data, jika mengetikan "c" maka akan melakukan pencarian data dengan memasukan keys 
```python
elif x.lower() == "l" :
        if a.items():
            print("="*79)
            print("|                                   DAFTAR MAHASISWA                               ") 
            print("="*79)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*79)
            i = 0 
            for y in a.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                    .format(y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
                print("="*79)
```
- code diatas untuk syntax melihat data, jika mengetikan "l" maka akan menampilkan keseluruhan dari data yang telah kita masukan 
```python
else:
            print("="*79)
            print("|                                   DAFTAR MAHASISWA                                ") 
            print("="*79)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*79)
            print("|                                   TIDAK ADA DATA                                  ") 
            print("="*79)
```
- code diatas untuk menampilkan "TIDAK ADA DATA", jika kita mengetikan "l" dan sebelumnya belum pernah menambahkankan atau memasukan data
```python
elif x.lower() == "k":
        print("Anda Telah Keluar")
        break
```
- code diatas untuk syntax keluar dari program, jika mengetikan "k" maka otomatis program selesai dan keluar
```python
 else:
        print("Pilih Menu Yang Tersedia")
```
- dan code yang terakhir adalah untuk syntax, jika kita mengetikan huruf yang diluar dari program, maka akan menampilkan "Pilih Menu Yang Tersedia"
## Berikut hasil dari program
- Menambahkan data dengan syntax "t" dan melihat data dengan syntax "l"
![gmabar12](ss/s11.PNG)
- Mengubah data dengan syntax "u" dan melihat data dengan syntax "l"
![gambar13](ss/s12.PNG)
- Mencari data dengan syntax "c" dan melihat data dengan syntax "l"
![gambar14](ss/s13.PNG)
- Menghapus data dengan syntax "h" dan melihat data dengan syntax "l"
![gambar15](ss/s14.PNG)
- Keluar dari program dengan syntax "k"
![gambar16](ss/s15.PNG)

# Sekian dan Trimakasih