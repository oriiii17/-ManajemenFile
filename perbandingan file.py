#membandingkan 2 file
def compare_files(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
        if line1 != line2:
            print(f"Perbedaan di baris {i}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}\n")

    if len(lines1) > len(lines2):
        print(f"File 1 memiliki {len(lines1)-len(lines2)} baris tambahan")
    elif len(lines2) > len(lines1):
        print(f"File 2 memiliki {len(lines2)-len(lines1)} baris tambahan")

if __name__ == "__main__":
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")
    compare_files(file1, file2)



def bandingkan_file(file1, file2):
    # Baca isi kedua file
    with open(file1) as f1, open(file2) as f2:
        baris1 = f1.readlines()
        baris2 = f2.readlines()

    print("\nHasil Perbandingan:")
    ada_perbedaan = False

    # Bandingkan setiap baris
    for nomor, (b1, b2) in enumerate(zip(baris1, baris2), start=1):
        if b1 != b2:
            print(f"Perbedaan di baris {nomor}:")
            print(f"File 1: {b1.strip()}")
            print(f"File 2: {b2.strip()}\n")
            ada_perbedaan = True

    # Cek jika jumlah baris berbeda
    if len(baris1) != len(baris2):
        print(f"Perbedaan jumlah baris:")
        print(f"File 1 punya {len(baris1)} baris")
        print(f"File 2 punya {len(baris2)} baris")
        ada_perbedaan = True

    if not ada_perbedaan:
        print("Kedua file sama persis!")

if __name__ == "__main__":
    print("Program Pembanding File Teks")
    nama_file1 = input("Masukkan nama file pertama: ")
    nama_file2 = input("Masukkan nama file kedua: ")
    bandingkan_file(nama_file1, nama_file2)
