import os

def tambah_data():
    jumlah = int(input("Masukkan jumlah alamat telepon: "))
    with open("buku_telepon.txt", "a") as file:
        for _ in range(jumlah):
            nama = input("Masukkan Nama: ")
            nomor = input("Masukkan nomor telepon: ")
            file.write(f"{nama},{nomor}\n")
    print("Data berhasil ditambahkan!\n")

def lihat_data():
    try:
        with open("buku_telepon.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("Belum ada data tersimpan.\n")
                return
            print("\n---Daftar Kontak---")
            for line in data:
                nama, nomor = line.strip().split(",")
                print(f"Nama: {nama}, Telp: {nomor}")
            print()
    except FileNotFoundError:
        print("File tidak ditemukan. Silakan tambah data terlebih dahulu.\n")

while True:
    print("---TUGAS!---")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Exit")
    
    try:
        pilihan = int(input("Masukkan nomor menu yang diinginkan: "))
        if pilihan == 1:
            print("\n---MENU TAMBAH DATA---")
            tambah_data()
        elif pilihan == 2:
            lihat_data()
        elif pilihan == 3:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")
    except ValueError:  # Error handling untuk input non-angka
        print("Input harus berupa angka!\n")