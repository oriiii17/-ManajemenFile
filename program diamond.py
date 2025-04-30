tinggi = int(input("Masukkan tinggi diamond: "))

with open("diamond.txt", "w") as file:
    # Bagian atas diamond
    for i in range(1, tinggi + 1, 2):
        spasi = (tinggi - i) // 2
        file.write(" " * spasi + "*" * i + "\n")
    
    # Bagian bawah diamond
    for i in range(tinggi - 2, 0, -2):
        spasi = (tinggi - i) // 2
        file.write(" " * spasi + "*" * i + "\n")

print("Diamond telah disimpan di diamond.txt")