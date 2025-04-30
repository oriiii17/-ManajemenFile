def main():
    print("Program Kuis Sederhana")
    nama_file = input("Nama file soal: ") or "soal.txt"
    
    try:
        with open(nama_file, 'r') as file:
            soal_jawaban = [line.strip().split('||') for line in file.readlines()]
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan!")
        return
    
    print(f"\nMemulai kuis dari file: {nama_file}\n")
    
    for soal, jawaban_benar in soal_jawaban:
        jawaban_benar = jawaban_benar.strip().lower()
        jawaban_user = input(f"{soal.strip()} Jawab: ").strip().lower()
        
        if jawaban_user == jawaban_benar:
            print("Jawaban benar!\n")
        else:
            print(f"Jawaban salah! Jawaban yang benar: {jawaban_benar}\n")

if __name__ == "__main__":
    main()
