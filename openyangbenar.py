inputan = input("Masukkan nama buku yang ingin dicari : ")
ini = open("daftarbuku.txt")
hasil = ini.readlines()
found = False  # Menandakan apakah buku sudah ditemukan

for line in hasil:
    line_temp = line.strip().split(",")
    if line_temp[0].lower() == inputan.lower():
        print('\nBuku ditemukan')
        print('Nama :', line_temp[0])
        print('Kode :', line_temp[1])
        print('Tahun rilis :', line_temp[2])
        print('Deskripsi :', line_temp[3])
        found = True
        break  # Hentikan pencarian setelah ditemukan

if not found:
    print("\nBuku tidak ditemukan")

ini.close()  # Tutup file setelah selesai
