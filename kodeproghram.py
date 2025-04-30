filename = input("Masukkan nama file: ")

try:
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From:"):
                count += 1
                # Konversi ke UPPERCASE dan hapus newline
                print(line.strip().upper())
    print(f"Total baris yang diawali 'From:': {count}")

except FileNotFoundError:
    print("File tidak ada!")

filename = input("Masukkan nama file output: ")

with open(filename, 'w') as file:
    for i in range(1, 6):
        file.write(f"Ini adalah baris ke-{i}\n")
    file.write("File ini dibuat menggunakan Python!")